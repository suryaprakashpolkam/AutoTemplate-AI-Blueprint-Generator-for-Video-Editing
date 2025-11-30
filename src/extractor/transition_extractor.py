import cv2
import numpy as np


class TransitionExtractor:
    def __init__(self, video_path):
        self.video_path = video_path
    
    def extract(self):
        cap = cv2.VideoCapture(self.video_path)
        transitions = []
        prev_frame = None
        frame_idx = 0
        
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break
            
            if prev_frame is not None:
                transition_type = self._detect_transition(prev_frame, frame)
                if transition_type:
                    transitions.append({
                        'timestamp': frame_idx / cap.get(cv2.CAP_PROP_FPS),
                        'type': transition_type
                    })
            
            prev_frame = frame
            frame_idx += 1
        
        cap.release()
        return transitions
    
    def _detect_transition(self, frame1, frame2):
        brightness1 = np.mean(cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY))
        brightness2 = np.mean(cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY))
        
        if abs(brightness1 - brightness2) > 50:
            if brightness2 < brightness1:
                return 'fade_to_black'
            else:
                return 'fade_from_black'
        
        diff = np.mean(np.abs(frame1.astype(float) - frame2.astype(float)))
        if diff > 40:
            return 'cut'
        
        return None
