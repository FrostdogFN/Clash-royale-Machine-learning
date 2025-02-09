import model
import utils
import pyautogui
import time
import json

# prits loading ai on the screen
def main():
    print("Starting Clash Royale AI...")
    
# Load counters and card cycle data
with open("counters.json", "r") as f:
    counters = json.load(f)

def get_best_counter(opponent_card):
    return counters.get(opponent_card, [])

def main():
    print("Starting Clash Royale AI...")

    # Load the trained model
    ai_model = model.load_model("models/trained_model.h5")

    # Track card cycle
    card_cycle = []

    # Give the game time to start before capturing the state
    time.sleep(5)

    while True:
        # Capture the game state (e.g., elixir, tower health, cards)
        game_state = utils.capture_game_state()
        elixir = game_state.get("elixir", 0)
        current_cards = game_state.get("current_cards", [])
        opponent_card = game_state.get("opponent_card", None)

        # Track cycle
        if len(card_cycle) >= 4:
            card_cycle.pop(0)
        card_cycle.append(current_cards)

        # Determine best move based on counters and elixir
        if opponent_card:
            possible_counters = get_best_counter(opponent_card)
            best_counter = None
            for counter in possible_counters:
                if counter in current_cards and elixir >= utils.get_elixir_cost(counter):
                    best_counter = counter
                    break
        else:
            best_counter = ai_model.predict(game_state)  # Fallback to AI decision

        # Play best move
        if best_counter:
            utils.perform_action(best_counter)

        # Add a small delay to mimic human-like speed
        time.sleep(1)  # Adjust based on how fast the game responds

if __name__ == "__main__":
    main()
