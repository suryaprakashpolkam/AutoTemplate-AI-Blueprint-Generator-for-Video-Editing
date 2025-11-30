import cv2
import numpy as np
from sklearn.cluster import KMeans


class ColorExtractor:
    def __init__(self, video_path, sample_rate=30):
        self.video_path = video_path
        self.sample_rate = sample_rate
    
    def extract(self):
        cap = cv2.VideoCapture(self.video_path)
        colors = []
        frame_idx = 0
        
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break
            
            if frame_idx % self.sample_rate == 0:
                dominant = self._get_dominant_colors(frame)
                colors.append({
                    'timestamp': frame_idx / cap.get(cv2.CAP_PROP_FPS),
                    'colors': dominant
                })
            
            frame_idx += 1
        
        cap.release()
        return colors
    
    def _get_dominant_colors(self, frame, k=5):
        pixels = frame.reshape(-1, 3)
        kmeans = KMeans(n_clusters=k, n_init=10)
        kmeans.fit(pixels)
        colors = kmeans.cluster_centers_.astype(int)
        return [{'rgb': color.tolist()} for color in colors]
