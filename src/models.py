import tensorflow as tf
from tensorflow.keras.models import load_model

def load_model(model_path):
    return load_model(model_path)

def detect_deepfakes(model, video_frames):
    return model.predict(video_frames)
