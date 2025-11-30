import cv2
import numpy as np


class PacingExtractor:
    def __init__(self, video_path, threshold=30.0):
        self.video_path = video_path
        self.threshold = threshold
    
    def extract(self):
        cap = cv2.VideoCapture(self.video_path)
        cuts = []
        prev_frame = None
        frame_idx = 0
        
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break
            
            if prev_frame is not None:
                diff = self._frame_difference(prev_frame, frame)
                if diff > self.threshold:
                    cuts.append({
                        'timestamp': frame_idx / cap.get(cv2.CAP_PROP_FPS),
                        'intensity': float(diff)
                    })
            
            prev_frame = frame
            frame_idx += 1
        
        cap.release()
        
        avg_cut_duration = self._calculate_avg_duration(cuts, frame_idx / cap.get(cv2.CAP_PROP_FPS))
        
        return {
            'cuts': cuts,
            'avg_scene_duration': avg_cut_duration,
            'total_cuts': len(cuts)
        }
    
    def _frame_difference(self, frame1, frame2):
        gray1 = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
        gray2 = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)
        return np.mean(np.abs(gray1.astype(float) - gray2.astype(float)))
    
    def _calculate_avg_duration(self, cuts, total_duration):
        if len(cuts) == 0:
            return total_duration
        return total_duration / (len(cuts) + 1)
