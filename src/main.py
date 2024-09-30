import models
import utils
from audio_feature_extraction import extract_audio_features
from video_feature_extraction import extract_video_features
from temporal_analysis import analyze_temporal_sequence

def main():

    model = models.load_model('models/xception_model.h5')
    lstm_model = models.load_model('models/lstm_model.h5')

    video_frames = extract_video_features('data/sample_videos/')
    audio_features = extract_audio_features('data/sample_audio/')

    visual_predictions = models.detect_deepfakes(model, video_frames)
    audio_predictions = analyze_temporal_sequence(lstm_model, audio_features)

    combined_results = utils.combine_audio_video_predictions(visual_predictions, audio_predictions)
    utils.display_results(combined_results)
    utils.save_results(combined_results, 'results/detection_results.csv')

if __name__ == '__main__':
    main()
