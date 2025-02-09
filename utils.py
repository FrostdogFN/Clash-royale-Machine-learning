# utils.py
# Helper functions for the AI

import numpy as np

def capture_game_state():
    # Capture the game state (this will depend on how you collect game data)
    # For now, returning a random state for example purposes
    return np.random.rand(10)

def perform_action(action):
    # Perform an action in the game (implement with the game API or manual input)
    print(f"Performing action: {action}")

def load_training_data():
    # Load training data (replace with your own data loading method)
    # For now, returning dummy data
    inputs = np.random.rand(100, 10)  # 100 examples, 10 features each
    labels = np.random.randint(2, size=(100, 1))  # Binary classification
    return {'inputs': inputs, 'labels': labels}
