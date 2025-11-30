import cv2
import numpy as np


class TextExtractor:
    def __init__(self, video_path):
        self.video_path = video_path
    
    def extract(self):
        cap = cv2.VideoCapture(self.video_path)
        text_regions = []
        frame_idx = 0
        
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break
            
            regions = self._detect_text_regions(frame)
            if regions:
                text_regions.append({
                    'timestamp': frame_idx / cap.get(cv2.CAP_PROP_FPS),
                    'regions': regions
                })
            
            frame_idx += 1
        
        cap.release()
        return text_regions
    
    def _detect_text_regions(self, frame):
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        _, thresh = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY)
        contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        
        regions = []
        for contour in contours:
            x, y, w, h = cv2.boundingRect(contour)
            if w > 50 and h > 20:
                regions.append({'x': int(x), 'y': int(y), 'width': int(w), 'height': int(h)})
        
        return regions
