# reinforcement_learning.py
import numpy as np
import random
import tensorflow as tf
from collections import deque

class DQNAgent:
    def __init__(self, state_size, action_size):
        self.state_size = state_size
        self.action_size = action_size
        self.memory = deque(maxlen=2000)  # Replay memory
        self.model = self._build_model()  # Neural network model

    def _build_model(self):
        # Build the model using LSTM
        model = tf.keras.Sequential([
            tf.keras.layers.LSTM(128, activation='relu', input_shape=(self.state_size,)),
            tf.keras.layers.Dense(256, activation='relu'),
            tf.keras.layers.Dense(self.action_size, activation='linear')  # Q-values output
        ])
        model.compile(optimizer=tf.keras.optimizers.Adam(lr=0.001), loss='mse')
        return model

    def act(self, state):
        # Epsilon-greedy action selection
        if np.random.rand() <= 0.1:  # Random action for exploration
            return random.randrange(self.action_size)
        act_values = self.model.predict(state)
        return np.argmax(act_values[0])  # Return the action with highest Q-value

    def remember(self, state, action, reward, next_state, done):
        # Store the experience in memory
        self.memory.append((state, action, reward, next_state, done))

    def replay(self, batch_size):
        # Sample a batch of experiences from memory
        if len(self.memory) < batch_size:
            return
        minibatch = random.sample(self.memory, batch_size)
        for state, action, reward, next_state, done in minibatch:
            target = reward
            if not done:
                target = reward + 0.95 * np.amax(self.model.predict(next_state)[0])  # Discounted future reward
            target_f = self.model.predict(state)
            target_f[0][action] = target  # Update Q-value
            self.model.fit(state, target_f, epochs=1, verbose=0)  # Train the model
