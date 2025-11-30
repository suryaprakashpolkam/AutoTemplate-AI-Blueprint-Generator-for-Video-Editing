import librosa
import numpy as np


class AudioExtractor:
    def __init__(self, video_path):
        self.video_path = video_path
    
    def extract(self):
        try:
            y, sr = librosa.load(self.video_path, sr=None)
            onset_frames = librosa.onset.onset_detect(y=y, sr=sr, units='time')
            
            peaks = []
            for timestamp in onset_frames:
                peaks.append({
                    'timestamp': float(timestamp),
                    'type': 'onset'
                })
            
            rms = librosa.feature.rms(y=y)[0]
            threshold = np.mean(rms) + np.std(rms)
            
            for i, value in enumerate(rms):
                if value > threshold:
                    timestamp = librosa.frames_to_time(i, sr=sr)
                    peaks.append({
                        'timestamp': float(timestamp),
                        'type': 'peak',
                        'intensity': float(value)
                    })
            
            peaks.sort(key=lambda x: x['timestamp'])
            return peaks
        
        except Exception as e:
            print(f"Audio extraction error: {e}")
            return []
