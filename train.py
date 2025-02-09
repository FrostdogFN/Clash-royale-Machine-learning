# train.py
# Training script for the Clash Royale AI

import model
import utils
import tensorflow as tf
from reinforcement_learning import DQNAgent

def train():
    state_size = 10  # Example: Number of features in the game state
    action_size = 10  # Example: Number of possible actions in the game

    agent = DQNAgent(state_size, action_size)  # Initialize the agent
    episodes = 1000  # Number of training episodes

    for e in range(episodes):
        state = utils.capture_game_state()
        state = np.reshape(state, [1, state_size])  # Reshape state for LSTM input

        for time in range(500):  # Limit the number of timesteps in one game
            action = agent.act(state)  # Choose an action using the policy (epsilon-greedy)
            next_state, reward, done = utils.simulate_action(action)  # Simulate the action's outcome
            next_state = np.reshape(next_state, [1, state_size])  # Reshape the next state

            agent.remember(state, action, reward, next_state, done)  # Store the experience
            state = next_state  # Move to the next state

            if done:  # End the episode if done
                break

        agent.replay(32)  # Sample from memory and train the model

        # Save model every 100 episodes
        if e % 100 == 0:
            print(f"Episode {e}/{episodes} completed.")
            model.save_model(agent.model, "models/trained_model.h5")

if __name__ == "__main__":
    train()
