class TemplateGenerator:
    def __init__(self, analysis_results):
        self.results = analysis_results
    
    def generate(self):
        template = {
            'metadata': {
                'fps': self.results['video_info']['fps'],
                'duration': self.results['video_info']['duration'],
                'frame_count': self.results['video_info']['frame_count']
            },
            'color_grading': self._simplify_colors(),
            'text_placements': self.results['text_placements'],
            'pacing': {
                'avg_scene_duration': self.results['pacing']['avg_scene_duration'],
                'total_cuts': self.results['pacing']['total_cuts'],
                'cuts': self.results['pacing']['cuts']
            },
            'transitions': self.results['transitions'],
            'audio_markers': self.results['audio_peaks']
        }
        
        return template
    
    def _simplify_colors(self):
        color_timeline = self.results['color_grading']
        if not color_timeline:
            return []
        
        simplified = []
        for entry in color_timeline[::5]:
            simplified.append({
                'timestamp': entry['timestamp'],
                'palette': entry['colors'][:3]
            })
        
        return simplified
