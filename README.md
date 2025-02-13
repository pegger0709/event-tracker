# Event Tracker

This AI tool automatically compiles a list of events occurring in the near future and saves them into a spreadsheet. It specifically focuses on conferences, summits, and meetups relevant to deeptech, brain-computer interfaces (BCI), and neurotechnology.

## Features

- Automated event discovery using AI agents
- Extracts key information including dates, locations, deadlines, and themes
- Saves data to a spreadsheet for easy tracking
- Monthly automatic updates
- Focus on scientific and technological events relevant to BCI and deeptech

## Prerequisites

- Python 3.9 or higher
- An Anthropic API key (for Claude AI)
- A Serper API key (for web search capabilities)
- Google Sheets API access (for spreadsheet updates)

## Setup

1. Clone the repository
```bash
git clone https://github.com/yourusername/event-tracker.git
cd event-tracker
```

2. Create a virtual environment:
```bash
python -m venv .venv
```

3. Activate the virtual environment:
   - Windows:
   ```bash
   .\.venv\Scripts\activate
   ```
   - Linux/Mac:
   ```bash
   source .venv/bin/activate
   ```

4. Install the project and its dependencies:
```bash
pip install -e .
```

5. Set up your environment variables:
   - Copy `.env.example` to `.env`
   - Add your API keys to `.env`:
   ```
   ANTHROPIC_API_KEY=your_anthropic_api_key
   SERPER_API_KEY=your_serper_api_key
   GOOGLE_SHEETS_CREDENTIALS_FILE=path/to/your/credentials.json
   ```

## Project Structure

```
event-tracker/
├── src/
│   └── event_tracker/
│       ├── config/        # Configuration files for agents and tasks
│       ├── tools/         # Custom tools for the AI agents
│       └── main.py        # Main execution script
├── tests/                 # Test files
└── ...
```

## Usage

Run the event tracker:
```bash
python src/event_tracker/main.py
```

## Development

1. Install development dependencies:
```bash
pip install -e ".[dev]"
```

2. Run tests:
```bash
pytest
```

## Contributing

1. Fork the repository
2. Create a new branch for your feature
3. Make your changes
4. Submit a pull request

## License

MIT

## Contact

Philip Egger

## Acknowledgments

- Built using [crewAI](https://docs.crewai.com/)