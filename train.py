# train.py
# Training script for the Clash Royale AI

import model
import utils
import tensorflow as tf

def train():
    # Load your training data
    data = utils.load_training_data()

    # Create and compile the model
    ai_model = model.create_model()

    # Train the model
    ai_model.fit(data['inputs'], data['labels'], epochs=10)

    # Save the trained model
    model.save_model(ai_model, "models/trained_model.h5")

if __name__ == "__main__":
    train()
