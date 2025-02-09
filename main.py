import model
import utils
import pyautogui
import time

def main():
    print("Starting Clash Royale AI...")

    # Load the trained model
    ai_model = model.load_model("models/trained_model.h5")

    # Give the game time to start before capturing the state
    time.sleep(5)

    while True:
        # Capture the game state (e.g., elixir, tower health, cards)
        game_state = utils.capture_game_state()

        # Predict the next action based on the game state
        action = ai_model.predict(game_state)

        # Perform the predicted action
        utils.perform_action(action)

        # Add a small delay to mimic human-like speed
        time.sleep(1)  # Adjust based on how fast the game responds

if __name__ == "__main__":
    main()

