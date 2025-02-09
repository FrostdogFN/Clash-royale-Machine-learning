import src.model as model
import src.utils as utils
import pyautogui
import time
import json

def click_battle_button():
    """
    Searches for the battle button on the screen and clicks it if found.
    """
    button_location = pyautogui.locateOnScreen("assets/battle_button.png", confidence=0.9)
    
    if button_location:
        print(f"Battle button found at {button_location}. Clicking...")
        pyautogui.click(button_location)
        time.sleep(2)
    else:
        print("Battle button not found.")

def get_best_counter(opponent_card):
    """Retrieve the best counters for a given opponent card."""
    with open("counters.json", "r") as f:
        counters = json.load(f)
    return counters.get(opponent_card, [])

def main():
    print("Starting Clash Royale AI...")
    
    click_battle_button()
    time.sleep(5)  # Wait for the match to start
    
    ai_model = model.load_model("models/trained_model.h5")
    card_cycle = []
    
    while True:
        game_state = utils.capture_game_state()
        elixir = game_state.get("elixir", 0)
        current_cards = game_state.get("current_cards", [])
        opponent_card = game_state.get("opponent_card", None)
        
        if len(card_cycle) >= 4:
            card_cycle.pop(0)
        card_cycle.append(current_cards)
        
        if opponent_card:
            possible_counters = get_best_counter(opponent_card)
            best_counter = None
            for counter in possible_counters:
                if counter in current_cards and elixir >= utils.get_elixir_cost(counter):
                    best_counter = counter
                    break
        else:
            best_counter = ai_model.predict(game_state)  # Fallback to AI decision
        
        if best_counter:
            utils.perform_action(best_counter)
        
        time.sleep(1)  # Mimic human-like response time

if __name__ == "__main__":
    main()
