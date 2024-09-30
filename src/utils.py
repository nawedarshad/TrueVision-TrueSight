import pandas as pd

def combine_audio_video_predictions(visual_preds, audio_preds):
    combined_preds = (visual_preds + audio_preds) / 2 
    return combined_preds

def display_results(predictions):
    for idx, prediction in enumerate(predictions):
        label = 'Deepfake' if prediction >= 0.5 else 'Real'
        print(f"Sample {idx+1}: {label} (Confidence: {prediction:.2f})")

def save_results(predictions, output_path):
    results = [{'Sample': i+1, 'Prediction': pred, 'Label': 'Deepfake' if pred >= 0.5 else 'Real'} 
               for i, pred in enumerate(predictions)]
    
    df = pd.DataFrame(results)
    df.to_csv(output_path, index=False)
    print(f"Results saved to {output_path}")
