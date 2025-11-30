# AutoTemplate

A single-purpose tool that analyzes uploaded videos and generates simplified, ready-to-use editing blueprints.

## Features

- **Color Grading Detection**: Extracts dominant colors and grading patterns
- **Text Placement Analysis**: Identifies text positions and timing
- **Pacing Detection**: Analyzes cut frequency and scene duration
- **Transition Recognition**: Detects transition types and timing
- **Audio Peak Detection**: Identifies audio peaks and sync points

## Installation

```bash
pip install -r requirements.txt
```

## Usage

```bash
python src/main.py --input video.mp4 --output template.json
```

## Output

Generates a structured JSON template containing:
- Color grading profiles
- Text placement coordinates and timing
- Scene pacing metrics
- Transition types and timestamps
- Audio peak markers
