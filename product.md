# Product Overview

AutoTemplate is a video analysis tool that transforms reference videos into editable style guides. It generates structured editing blueprints that allow users to recreate the same style without needing professional editing expertise.

## Purpose

Analyzes videos to extract reusable editing patterns and outputs a comprehensive JSON template that serves as a ready-to-use editing blueprint. AutoTemplate transforms any reference video into an editable style guide in seconds.

## Core Features

- Color grading detection using K-means clustering
- Text placement and timing analysis
- Scene pacing and cut detection
- Transition type identification
- Audio peak and onset detection

## Output Format

JSON template containing:
- **Color grading presets**: Dominant color palettes and grading patterns
- **Suggested fonts**: Text placement coordinates and timing
- **Timing markers for sound effects**: Audio peaks and onset detection
- **High-level timeline structure**: Scene pacing metrics, cuts, and transitions
- **Video metadata**: fps, duration, frame count

The output enables users to recreate professional video styles by providing all the essential editing parameters extracted from reference videos.
