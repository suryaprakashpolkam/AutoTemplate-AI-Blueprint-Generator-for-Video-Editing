import argparse
import json
from pathlib import Path
from analyzer.video_analyzer import VideoAnalyzer
from template.template_generator import TemplateGenerator


def main():
    parser = argparse.ArgumentParser(description='AutoTemplate - Video Analysis Tool')
    parser.add_argument('--input', '-i', required=True, help='Input video file path')
    parser.add_argument('--output', '-o', default='template.json', help='Output template file path')
    args = parser.parse_args()
    
    input_path = Path(args.input)
    if not input_path.exists():
        print(f"Error: Video file not found: {input_path}")
        return
    
    print(f"Analyzing video: {input_path}")
    analyzer = VideoAnalyzer(str(input_path))
    analysis_results = analyzer.analyze()
    
    print("Generating template...")
    generator = TemplateGenerator(analysis_results)
    template = generator.generate()
    
    with open(args.output, 'w') as f:
        json.dump(template, f, indent=2)
    
    print(f"Template saved to: {args.output}")


if __name__ == '__main__':
    main()
