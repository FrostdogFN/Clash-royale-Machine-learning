import tensorflow as tf

def load_model(model_path):
    """
    Load the pre-trained model from the specified file path.
    """
    # Load the model (ensure it's a Keras model)
    model = tf.keras.models.load_model(model_path)
    return model
