import model
import utils
import pyautogui
import time
import json

# Load counters and card cycle data
with open("counters.json", "r") as f:
    counters = json.load(f)

def get_best_counter(opponent_card, current_cards, elixir):
    """Returns the best counter based on the opponent's card and available cards."""
    possible_counters = counters.get(opponent_card, [])
    for counter in possible_counters:
        if counter in current_cards and elixir >= utils.get_elixir_cost(counter):
            return counter
    return None

def capture_and_update_state(card_cycle):
    """Captures game state and updates card cycle."""
    game_state = utils.capture_game_state()
    elixir = game_state.get("elixir", 0)
    current_cards = game_state.get("current_cards", [])
    opponent_card = game_state.get("opponent_card", None)

    if len(card_cycle) >= 4:
        card_cycle.pop(0)
    card_cycle.append(current_cards)

    return elixir, current_cards, opponent_card, card_cycle

def make_best_move(ai_model, elixir, current_cards, opponent_card):
    """Determines the best move based on counters or AI prediction."""
    if opponent_card:
        return get_best_counter(opponent_card, current_cards, elixir)
    else:
        return ai_model.predict({"elixir": elixir, "current_cards": current_cards})  # AI model prediction fallback

def main():
    print("Starting Clash Royale AI...")

    # Load the trained model
    ai_model = model.load_model("models/trained_model.h5")

    # Track card cycle
    card_cycle = []

    # Give the game time to start before capturing the state
    time.sleep(5)

    while True:
        # Capture the game state and update card cycle
        elixir, current_cards, opponent_card, card_cycle = capture_and_update_state(card_cycle)

        # Determine best move
        best_move = make_best_move(ai_model, elixir, current_cards, opponent_card)

        # Perform the best move if one exists
        if best_move:
            utils.perform_action(best_move)

        # Add a small delay to mimic human-like speed
        time.sleep(1)  # Adjust based on how fast the game responds

if __name__ == "__main__":
    main()
