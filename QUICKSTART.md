# Quick Start Guide

## Installation

1. **Install Python dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
   
   Or if you're using Python 3:
   ```bash
   pip3 install -r requirements.txt
   ```

2. **Verify installation:**
   ```bash
   python3 main.py --help
   ```

## Basic Usage

### Command Line

**Get information about a place:**
```bash
python3 main.py "Paris"
```

**Get JSON output:**
```bash
python3 main.py "Tokyo" --format json
```

**Get text output (default):**
```bash
python3 main.py "New York" --format text
```

### Python Code

```python
from src.agents.tourism_agent import TourismAgent

# Create agent
agent = TourismAgent()

# Get information
response = agent.process("Paris")

# Format output
print(agent.format_response(response, format_type="text"))
```

## Example Queries

Try these places:
- `"Paris"` - Major European city
- `"Tokyo"` - Major Asian city  
- `"New York"` - Major US city
- `"Barcelona"` - European city with many attractions
- `"Sydney"` - Australian city
- `"InvalidPlace123"` - Test error handling

## Troubleshooting

### ModuleNotFoundError: No module named 'requests'
**Solution:** Install dependencies:
```bash
pip install requests
```

### API Timeout Errors
- Check your internet connection
- Overpass API can be slow (10-30 seconds) - be patient
- Some APIs may have rate limits

### No Attractions Found
- Some remote places may have limited data in OpenStreetMap
- Try larger cities for better results
- The system will still return weather information

## Next Steps

- Read the full [README.md](README.md) for detailed documentation
- Check [PLAN.md](PLAN.md) for architecture details
- Run `python3 example.py` to see more examples

