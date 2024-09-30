import librosa
import numpy as np

def extract_audio_features(audio_folder_path):

    audio_features = []
    for audio_file in os.listdir(audio_folder_path):
        audio_path = os.path.join(audio_folder_path, audio_file)
        audio, sr = librosa.load(audio_path)
        

        fft_features = np.abs(np.fft.fft(audio))
        

        hubert_features = extract_hubert_features(audio)
        
        audio_features.append(np.concatenate([fft_features, hubert_features]))
    
    return np.array(audio_features)

def extract_hubert_features(audio):

    return np.zeros(100) 
