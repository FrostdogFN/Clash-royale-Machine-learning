# utils.py
import pyautogui
import time
import numpy as np
import logging
from mss import mss
from PIL import Image

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

class Humanizer:
    def __init__(self):
        """
        Simulate human-like behavior with delays and variability.
        """
        self.reaction_mean = 0.2  # Average reaction time (200ms)
        self.reaction_std = 0.05  # Variability in reaction time
        self.position_std = 5     # Pixel position variability
        self.mistake_rate = 0.1   # 10% chance of making a mistake

    def human_delay(self):
        """
        Simulate human reaction time with random variability.
        """
        delay = abs(np.random.normal(self.reaction_mean, self.reaction_std))
        time.sleep(delay)

    def human_position(self, x: int, y: int) -> tuple[int, int]:
        """
        Add variability to click positions.
        :param x: Target x-coordinate
        :param y: Target y-coordinate
        :return: Adjusted (x, y) coordinates
        """
        return (
            int(x + np.random.normal(0, self.position_std)),
            int(y + np.random.normal(0, self.position_std))
        )

    def should_make_mistake(self) -> bool:
        """
        Randomly decide if the bot should make a "mistake."
        :return: True if a mistake should be made
        """
        return random.random() < self.mistake_rate

def capture_game_state():
    """
    Capture the current game state (screenshot or specific game data).
    :return: Dictionary containing game state data
    """
    try:
        # Take a screenshot of the current screen
        with mss() as sct:
            screenshot = sct.grab(sct.monitors[1])
            img = Image.frombytes("RGB", screenshot.size, screenshot.rgb)
            game_state = np.array(img)

        # Example: Extract elixir and cards from the screenshot (placeholder logic)
        elixir = 10  # Replace with actual elixir detection logic
        current_cards = ["Knight", "Archers", "Fireball"]  # Replace with actual card detection logic

        return {
            "elixir": elixir,
            "current_cards": current_cards,
            "screenshot": game_state
        }
    except Exception as e:
        logging.error(f"Error capturing game state: {e}")
        return None

def perform_action(action: str):
    """
    Perform the action based on the AI's decision.
    :param action: Action to perform (e.g., "attack", "defend")
    """
    humanizer = Humanizer()
    humanizer.human_delay()

    if action == 'attack':
        x, y = humanizer.human_position(100, 200)  # Example coordinates
        pyautogui.click(x, y)
    elif action == 'defend':
        x, y = humanizer.human_position(300, 400)  # Example coordinates
        pyautogui.click(x, y)
    elif action == 'move':
        x, y = humanizer.human_position(500, 600)  # Example coordinates
        pyautogui.moveTo(x, y)
    else:
        logging.warning(f"Unknown action: {action}")
