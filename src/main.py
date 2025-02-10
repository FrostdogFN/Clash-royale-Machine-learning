import src.model as model
import src.utils as utils
import pyautogui
import time
import json
import logging
import sys
from typing import Optional, List

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filename="clash_royale_ai.log"
)

# Constants
BATTLE_BUTTON_IMAGE = "assets/battle_button.png"
COUNTERS_FILE = "counters.json"
MODEL_PATH = "models/trained_model.h5"

class ClashRoyaleAI:
    def __init__(self):
        """Initialize the AI with necessary components."""
        self.ai_model = model.load_model(MODEL_PATH)
        self.card_cycle: List[str] = []
        self.humanizer = utils.Humanizer()

    def click_battle_button(self) -> bool:
        """
        Search for the battle button and click it if found.
        Returns True if successful, False otherwise.
        """
        try:
            button_location = pyautogui.locateOnScreen(BATTLE_BUTTON_IMAGE, confidence=0.9)
            if button_location:
                logging.info(f"Battle button found at {button_location}. Clicking...")
                self.humanizer.human_delay()
                pyautogui.click(button_location)
                return True
            else:
                logging.warning("Battle button not found.")
                return False
        except Exception as e:
            logging.error(f"Error clicking battle button: {e}")
            return False

    def get_best_counter(self, opponent_card: str) -> List[str]:
        """
        Retrieve the best counters for a given opponent card.
        Returns an empty list if no counters are found.
        """
        try:
            with open(COUNTERS_FILE, "r") as f:
                counters = json.load(f)
            return counters.get(opponent_card, [])
        except Exception as e:
            logging.error(f"Error loading counters: {e}")
            return []

    def run(self):
        """Main loop for the Clash Royale AI."""
        logging.info("Starting Clash Royale AI...")

        if not self.click_battle_button():
            logging.error("Failed to start battle. Exiting.")
            sys.exit(1)

        time.sleep(5)  # Wait for the match to start

        while True:
            try:
                # Capture game state
                game_state = utils.capture_game_state()
                if not game_state:
                    logging.warning("Failed to capture game state. Retrying...")
                    time.sleep(1)
                    continue

                # Update card cycle
                elixir = game_state.get("elixir", 0)
                current_cards = game_state.get("current_cards", [])
                opponent_card = game_state.get("opponent_card", None)

                if len(self.card_cycle) >= 4:
                    self.card_cycle.pop(0)
                self.card_cycle.append(current_cards)

                # Determine best counter
                best_counter: Optional[str] = None
                if opponent_card:
                    possible_counters = self.get_best_counter(opponent_card)
                    for counter in possible_counters:
                        if counter in current_cards and elixir >= utils.get_elixir_cost(counter):
                            best_counter = counter
                            break
                else:
                    # Fallback to AI decision
                    best_counter = self.ai_model.predict(game_state)

                # Perform action
                if best_counter:
                    logging.info(f"Playing card: {best_counter}")
                    utils.perform_action(best_counter)
                else:
                    logging.info("No valid counter found. Waiting...")

                # Human-like delay
                self.humanizer.human_delay()

            except KeyboardInterrupt:
                logging.info("Exiting Clash Royale AI.")
                break
            except Exception as e:
                logging.error(f"Unexpected error: {e}")
                time.sleep(1)  # Prevent spamming errors

if __name__ == "__main__":
    ai = ClashRoyaleAI()
    ai.run()
