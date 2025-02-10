# model.py
import tensorflow as tf
import json
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def load_model(model_path: str):
    """
    Load the pre-trained model from the specified file path.
    :param model_path: Path to the model file
    :return: Loaded Keras model
    """
    try:
        model = tf.keras.models.load_model(model_path)
        logging.info(f"Model loaded successfully from {model_path}.")
        return model
    except Exception as e:
        logging.error(f"Error loading model: {e}")
        raise

def create_model(input_shape: tuple, num_actions: int):
    """
    Create a new CNN model for Clash Royale action prediction.
    :param input_shape: Shape of input frames (height, width, channels)
    :param num_actions: Number of possible actions
    :return: Compiled Keras model
    """
    model = tf.keras.Sequential([
        tf.keras.layers.Conv2D(32, (3, 3), activation='relu', input_shape=input_shape),
        tf.keras.layers.MaxPooling2D((2, 2)),
        tf.keras.layers.Dropout(0.25),

        tf.keras.layers.Conv2D(64, (3, 3), activation='relu'),
        tf.keras.layers.MaxPooling2D((2, 2)),
        tf.keras.layers.Dropout(0.25),

        tf.keras.layers.Flatten(),
        tf.keras.layers.Dense(128, activation='relu'),
        tf.keras.layers.Dense(num_actions, activation='softmax')
    ])

    model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
    logging.info("New model created and compiled successfully.")
    return model

# Clash Royale counters dictionary
counters = {
    "Knight": ["Mini P.E.K.K.A", "P.E.K.K.A", "Skeleton Army"],
    "Mini P.E.K.K.A": ["Swarm Units", "Inferno Tower", "Inferno Dragon"],
    # ... (rest of your counters dictionary)
}

def save_counters_to_json():
    """
    Save the counters dictionary to a JSON file.
    """
    try:
        with open("counters.json", "w") as f:
            json.dump(counters, f, indent=4)
        logging.info("Counters saved to counters.json.")
    except Exception as e:
        logging.error(f"Error saving counters to JSON: {e}")

def get_best_counter(opponent_card: str) -> list:
    """
    Retrieve the best counters for a given opponent card.
    :param opponent_card: Name of the opponent's card
    :return: List of counters (empty if no counters found)
    """
    return counters.get(opponent_card, [])

# Save counters to JSON file on module load
save_counters_to_json()
