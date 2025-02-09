# Clash Royale AI

This project is an AI for playing **Clash Royale** using machine learning techniques. The AI interacts with the game by recognizing the current state of the game (e.g., elixir, cards, tower health) and making decisions based on a trained model. The goal is to make the AI capable of playing the game autonomously by predicting the next best actions.

## Features

- **Game State Recognition**: Captures the game’s current state by taking screenshots and analyzing them.
- **AI Model**: Uses a trained machine learning model to predict the best actions based on the current game state.
- **Auto-Play**: The AI can automatically play the game by simulating clicks and actions based on the model's predictions.
- **Customizable Models**: Ability to train different models and use them within the system.

## Disclaimer

**USE AT YOUR OWN RISK**: This project is not officially endorsed by Supercell or affiliated with Clash Royale in any way. It is intended for educational and experimental purposes only. By using this AI, you acknowledge that it may lead to account penalties, including but not limited to being banned from the game. 

I am **not responsible** for any consequences, including account bans or other sanctions, that may arise from using this software. Use it at your own discretion.

## Setup Instructions

### Requirements

- Python 3.x
- Libraries:
  - TensorFlow
  - Keras
  - OpenCV
  - PyAutoGUI
  - NumPy
  - Matplotlib
  - H5py
- A **trained model** (models/trained_model.h5)

### Install Dependencies

1. Clone the repository:
   ```bash
   git clone https://github.com/FrostdogFN/Clash-royale-Machine-learning.git
   cd Clash-royale-Machine-learning
