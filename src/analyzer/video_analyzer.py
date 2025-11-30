import cv2
from extractor.color_extractor import ColorExtractor
from extractor.text_extractor import TextExtractor
from extractor.pacing_extractor import PacingExtractor
from extractor.transition_extractor import TransitionExtractor
from extractor.audio_extractor import AudioExtractor


class VideoAnalyzer:
    def __init__(self, video_path):
        self.video_path = video_path
        self.cap = cv2.VideoCapture(video_path)
        self.fps = self.cap.get(cv2.CAP_PROP_FPS)
        self.frame_count = int(self.cap.get(cv2.CAP_PROP_FRAME_COUNT))
        self.duration = self.frame_count / self.fps if self.fps > 0 else 0
    
    def analyze(self):
        print("Extracting color grading...")
        color_data = ColorExtractor(self.video_path).extract()
        
        print("Detecting text placements...")
        text_data = TextExtractor(self.video_path).extract()
        
        print("Analyzing pacing...")
        pacing_data = PacingExtractor(self.video_path).extract()
        
        print("Identifying transitions...")
        transition_data = TransitionExtractor(self.video_path).extract()
        
        print("Detecting audio peaks...")
        audio_data = AudioExtractor(self.video_path).extract()
        
        return {
            'video_info': {
                'fps': self.fps,
                'duration': self.duration,
                'frame_count': self.frame_count
            },
            'color_grading': color_data,
            'text_placements': text_data,
            'pacing': pacing_data,
            'transitions': transition_data,
            'audio_peaks': audio_data
        }
    
    def __del__(self):
        if hasattr(self, 'cap'):
            self.cap.release()
