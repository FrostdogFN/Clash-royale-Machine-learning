import model
import utils
import pyautogui
import time

def click_battle_button():
    """
    This function searches for the battle button on the screen
    and clicks it if found.
    """
    # Locate the battle button on the screen
    button_location = pyautogui.locateOnScreen("assets/battle_button.png", confidence=0.9)

    if button_location:
        print(f"Battle button found at {button_location}. Clicking...")
        pyautogui.click(button_location)  # Click the button
        time.sleep(2)  # Wait a bit before doing anything else
    else:
        print("Battle button not found.")

def main():
    print("Starting Clash Royale AI...")

    # Click the battle button to enter the game
    click_battle_button()

    # Give the game time to start before capturing the state
    time.sleep(5)

    # Load the trained model
    ai_model = model.load_model("models/trained_model.h5")

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
