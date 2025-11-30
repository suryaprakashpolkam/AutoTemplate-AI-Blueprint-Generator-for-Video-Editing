# Technology Stack

## Language

Python 3.x

## Core Dependencies

- **opencv-python** (>=4.8.0): Video processing and frame analysis
- **numpy** (>=1.24.0): Numerical operations and array processing
- **moviepy** (>=1.0.3): Video file handling
- **scikit-learn** (>=1.3.0): K-means clustering for color extraction
- **librosa** (>=0.10.0): Audio analysis and onset detection
- **Pillow** (>=10.0.0): Image processing

## Common Commands

### Installation
```bash
pip install -r requirements.txt
```

### Run Analysis
```bash
python src/main.py --input video.mp4 --output template.json
```

### Command Line Arguments
- `--input` or `-i`: Input video file path (required)
- `--output` or `-o`: Output template file path (default: template.json)

## Build System

Standard Python package with pip-based dependency management. No build step required.
