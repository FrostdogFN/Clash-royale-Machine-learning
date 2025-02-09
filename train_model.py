import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# Function to create the model
def create_model(state_size, action_size):
    model = Sequential()
    model.add(Dense(64, input_dim=state_size, activation='relu'))  # Hidden layer 1
    model.add(Dense(64, activation='relu'))  # Hidden layer 2
    model.add(Dense(action_size, activation='softmax'))  # Output layer
    model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
    return model

# Example data for training (You need to replace this with actual game data)
game_states = np.array([
    [0.1, 0.5, 0.3, 0.2],
    [0.2, 0.4, 0.3, 0.1],
    # More game states...
])

actions = np.array([
    [1, 0, 0, 0],  # One-hot encoded actions
    [0, 1, 0, 0],
    # More actions...
])

# Define the state and action sizes
state_size = len(game_states[0])
action_size = len(actions[0])

# Create and train the model
model = create_model(state_size, action_size)
model.fit(game_states, actions, epochs=10, batch_size=32)

# Save the trained model
model.save('models/trained_model.h5')
print("Model trained and saved as 'models/trained_model.h5'")
