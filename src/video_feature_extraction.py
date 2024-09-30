import cv2
import numpy as np
from models import load_model

def extract_video_features(video_folder_path):

    video_frames = []
    for video_file in os.listdir(video_folder_path):
        video_path = os.path.join(video_folder_path, video_file)
        cap = cv2.VideoCapture(video_path)

        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break
            
            frame = preprocess_frame(frame)
            video_frames.append(frame)
        
        cap.release()

    return np.array(video_frames)

def preprocess_frame(frame):

    frame = cv2.resize(frame, (299, 299))
    frame = frame.astype(np.float32) / 255.0
    return frame
