# Project Structure

## Architecture Pattern

Modular extraction pipeline with separation of concerns:
- **Extractors**: Individual feature extraction modules
- **Analyzer**: Orchestrates extractors and aggregates results
- **Template Generator**: Transforms analysis into simplified output format

## Folder Organization

```
.kiro/
└── steering/                  # AI assistant steering rules (DO NOT gitignore)
    ├── product.md
    ├── tech.md
    └── structure.md
src/
├── main.py                    # Entry point, CLI argument parsing
├── analyzer/
│   ├── video_analyzer.py      # Orchestrates all extractors
│   └── __init__.py
├── extractor/
│   ├── audio_extractor.py     # Audio peak and onset detection
│   ├── color_extractor.py     # Dominant color extraction
│   ├── pacing_extractor.py    # Cut detection and scene timing
│   ├── text_extractor.py      # Text placement analysis
│   ├── transition_extractor.py # Transition type detection
│   └── __init__.py
└── template/
    ├── template_generator.py  # Simplifies analysis into template
    └── __init__.py
```

**Important**: The `.kiro/` directory must be committed to version control and should NOT be gitignored. It contains steering rules that guide AI assistants working with this codebase.

## Code Conventions

### Extractor Pattern
All extractors follow a consistent interface:
- Constructor accepts `video_path` and optional parameters
- Single `extract()` method returns structured data
- Handle OpenCV VideoCapture lifecycle (open/release)
- Return empty list/dict on errors with error logging

### Data Flow
1. `main.py` validates input and creates VideoAnalyzer
2. VideoAnalyzer instantiates all extractors and calls `extract()`
3. Results aggregated into dictionary with standardized keys
4. TemplateGenerator simplifies data (e.g., downsampling color timeline)
5. Final JSON written to output file

### Naming Conventions
- Classes: PascalCase (e.g., `ColorExtractor`)
- Methods: snake_case (e.g., `extract()`, `_get_dominant_colors()`)
- Private methods: prefix with underscore
- Module names: snake_case matching class name

### Resource Management
- Use context managers or explicit cleanup for video captures
- Implement `__del__` for VideoAnalyzer to release resources
- Handle exceptions in extractors to prevent pipeline failures
