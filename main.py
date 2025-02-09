# main.py
# Main script to run the Clash Royale AI

import model
import utils

def main():
    print("Starting Clash Royale AI...")
    # Load trained model
    ai_model = model.load_model("models/trained_model.h5")
    
    # Run AI in a game loop
    while True:
        game_state = utils.capture_game_state()
        action = ai_model.predict(game_state)
        utils.perform_action(action)

if __name__ == "__main__":
    main()