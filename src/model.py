import tensorflow as tf
import json

def load_model(model_path):
    """
    Load the pre-trained model from the specified file path.
    """
    model = tf.keras.models.load_model(model_path)
    return model

# Clash Royale counters dictionary
counters = {
    "Knight": ["Mini P.E.K.K.A", "P.E.K.K.A", "Skeleton Army"],
    "Mini P.E.K.K.A": ["Swarm Units", "Inferno Tower", "Inferno Dragon"],
    "P.E.K.K.A": ["Inferno Tower", "Inferno Dragon", "Swarm Units", "Kite Units (e.g., Ice Golem)"],
    "Skeleton Army": ["Zap", "Log", "Arrows"],
    "Goblin Barrel": ["Log", "Arrows", "Valkyrie"],
    "Hog Rider": ["Cannon", "Tornado", "Mini P.E.K.K.A"],
    "Balloon": ["Tornado", "Inferno Tower", "Musketeer"],
    "Golem": ["Inferno Tower", "Inferno Dragon", "P.E.K.K.A"],
    "Giant": ["Inferno Tower", "Mini P.E.K.K.A", "P.E.K.K.A"],
    "Royal Giant": ["Inferno Tower", "Mini P.E.K.K.A", "P.E.K.K.A"],
    "Three Musketeers": ["Fireball", "Poison", "Lightning"],
    "Elite Barbarians": ["P.E.K.K.A", "Mini P.E.K.K.A", "Tornado"],
    "Prince": ["Swarm Units", "Inferno Tower", "P.E.K.K.A"],
    "Dark Prince": ["P.E.K.K.A", "Inferno Tower", "Mini P.E.K.K.A"],
    "Goblin Gang": ["Log", "Arrows", "Valkyrie"],
    "Bats": ["Zap", "Arrows", "Baby Dragon"],
    "Electro Wizard": ["Fireball", "Poison", "Lightning"],
    "Mega Minion": ["Musketeer", "Minions", "Baby Dragon"],
    "Hunter": ["Fireball", "Lightning", "P.E.K.K.A"],
    "Witch": ["Poison", "Fireball", "Lightning"],
    "Night Witch": ["Poison", "Fireball", "Lightning"],
    "Baby Dragon": ["Musketeer", "Electro Wizard", "Mega Minion"],
    "Inferno Dragon": ["Electro Wizard", "Lightning", "Zap"],
    "Lava Hound": ["Inferno Tower", "Mega Minion", "Musketeer"],
    "Graveyard": ["Poison", "Valkyrie", "Baby Dragon"],
    "Royal Hogs": ["Fireball", "Valkyrie", "Bomb Tower"],
    "X-Bow": ["P.E.K.K.A", "Golem", "Rocket"],
    "Mortar": ["P.E.K.K.A", "Golem", "Rocket"],
    "Cannon Cart": ["P.E.K.K.A", "Mini P.E.K.K.A", "Inferno Tower"],
    "Sparky": ["Electro Wizard", "Zap", "Lightning"],
    "Goblin Giant": ["Inferno Tower", "Mini P.E.K.K.A", "P.E.K.K.A"],
    "Fisherman": ["Swarm Units", "Fireball", "Lightning"],
    "Zappies": ["Fireball", "Poison", "Lightning"],
    "Royal Recruits": ["Fireball", "Poison", "Valkyrie"],
    "Ram Rider": ["Mini P.E.K.K.A", "Inferno Tower", "Tornado"],
    "Electro Giant": ["Inferno Tower", "P.E.K.K.A", "Rocket"],
    "Goblin Drill": ["Valkyrie", "Swarm Units", "Bomb Tower"],
    "Phoenix": ["Lightning", "Poison", "Baby Dragon"],
    "Monk": ["P.E.K.K.A", "Mini P.E.K.K.A", "Inferno Tower"],
    "Mighty Miner": ["P.E.K.K.A", "Inferno Tower", "Mini P.E.K.K.A"],
    "Elixir Golem": ["Inferno Tower", "Mini P.E.K.K.A", "P.E.K.K.A"],
    "Archers": ["Poison", "Fireball", "Baby Dragon"],
    "Musketeer": ["Fireball", "Lightning", "Poison"],
    "Wizard": ["Fireball", "Lightning", "Poison"],
    "Executioner": ["Lightning", "Rocket", "P.E.K.K.A"],
    "Bowler": ["Inferno Tower", "Mini P.E.K.K.A", "P.E.K.K.A"],
    "Magic Archer": ["Fireball", "Lightning", "Poison"],
    "Bandit": ["Swarm Units", "P.E.K.K.A", "Mini P.E.K.K.A"],
    "Battle Healer": ["P.E.K.K.A", "Inferno Tower", "Mini P.E.K.K.A"],
    "Skeleton Barrel": ["Log", "Arrows", "Baby Dragon"],
    "Firecracker": ["Poison", "Fireball", "Arrows"],
    "Mother Witch": ["Lightning", "Poison", "Fireball"],
    "Goblin Cage": ["P.E.K.K.A", "Mini P.E.K.K.A", "Inferno Tower"],
    "Cannon": ["Golem", "P.E.K.K.A", "Rocket"],
    "Inferno Tower": ["Zap", "Electro Wizard", "Lightning"],
    "Tornado": ["Fireball", "Poison", "Lightning"],
    "Rocket": ["Three Musketeers", "Sparky", "Inferno Tower"],
    "Poison": ["Graveyard", "Swarm Units", "Buildings"],
    "Lightning": ["Three Musketeers", "Hunter", "Electro Wizard"],
    "Fireball": ["Archers", "Musketeer", "Magic Archer"],
    "Arrows": ["Swarm Units", "Minions", "Goblin Gang"],
    "Zap": ["Skeleton Army", "Inferno Dragon", "Bats"],
    "Log": ["Goblin Barrel", "Skeleton Army", "Goblin Gang"]
}

# Save the counters to a JSON file
with open("counters.json", "w") as f:
    json.dump(counters, f, indent=4)

def get_best_counter(opponent_card):
    """Retrieve the best counters for a given opponent card."""
    return counters.get(opponent_card, [])
