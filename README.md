# Multi-Agent Tourism System

A sophisticated multi-agent system that provides weather information and tourist attraction suggestions for any place in the world.

## 🌟 Features

- **🌐 Modern Web Interface**: Beautiful, responsive web UI with weather forecast cards and attraction grids
- **Intelligent Place Recognition**: Uses Nominatim API to geocode place names and validate their existence
- **Weather Information**: Real-time current weather and 7-day forecast via Open-Meteo API
- **Tourist Attractions**: Finds up to 5 nearby tourist attractions using Overpass API
- **Error Handling**: Graceful handling of non-existent places and API failures
- **Multiple Output Formats**: Web UI, JSON, and human-readable text output
- **Clean Architecture**: Modular design with separate agents and API clients

## 🏗️ Architecture

The system follows a multi-agent architecture:

```
User Input (Place Name)
    ↓
Tourism AI Agent (Parent Orchestrator)
    ├──→ Nominatim API (Geocoding)
    ├──→ Weather Agent (Child Agent 1)
    │   └──→ Open-Meteo API
    └──→ Places Agent (Child Agent 2)
        └──→ Overpass API
    ↓
Consolidated Response
```

### Components

1. **Tourism Agent** (Parent): Orchestrates the entire system, coordinates child agents
2. **Weather Agent** (Child 1): Fetches current weather and forecast
3. **Places Agent** (Child 2): Finds tourist attractions near the location
4. **API Clients**: Handle all external API communications

## 📋 Requirements

- Python 3.7+
- Internet connection (for API access)

## 🚀 Installation

1. Clone or download this repository

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## 💻 Usage

### 🌐 Web Interface (Recommended)

The easiest way to use the system is through the modern web interface:

1. **Install Flask:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Start the web server:**
   ```bash
   python app.py
   ```

3. **Open your browser:**
   Navigate to `http://localhost:5000`

4. **Search for places:**
   - Enter any place name in the search box
   - View beautiful weather forecast cards
   - Browse tourist attractions in a grid layout
   - All results update in real-time

### Command Line Interface

Basic usage:
```bash
python main.py "Paris"
```

With JSON output:
```bash
python main.py "Tokyo" --format json
```

With text output (default):
```bash
python main.py "New York" --format text
```

### Programmatic Usage

```python
from src.agents.tourism_agent import TourismAgent

# Initialize the agent
agent = TourismAgent()

# Process a place
response = agent.process("Paris")

# Format output
print(agent.format_response(response, format_type="text"))
```

## 📊 Example Output

### Text Format
```
============================================================
📍 Paris, Île-de-France, France
   Country: France
   Coordinates: 48.8566, 2.3522
============================================================

🌤️  CURRENT WEATHER
------------------------------------------------------------
Temperature: 15.5°C
Condition: Partly cloudy
Wind Speed: 12.3 km/h

📅 FORECAST
------------------------------------------------------------
2024-01-15: 12.0°C - 18.0°C, Partly cloudy
2024-01-16: 10.0°C - 16.0°C, Overcast
2024-01-17: 11.0°C - 17.0°C, Clear sky

🏛️  TOURIST ATTRACTIONS (5 found)
------------------------------------------------------------
1. Eiffel Tower (attraction) (2.30 km away)
2. Louvre Museum (museum) (1.50 km away)
3. Notre-Dame de Paris (attraction) (3.20 km away)
4. Arc de Triomphe (monument) (4.10 km away)
5. Champs-Élysées (attraction) (3.80 km away)

============================================================
```

### JSON Format
```json
{
  "place": {
    "name": "Paris",
    "display_name": "Paris, Île-de-France, France",
    "country": "France",
    "coordinates": {
      "latitude": 48.8566,
      "longitude": 2.3522
    }
  },
  "weather": {
    "current": {
      "temperature": 15.5,
      "condition": "Partly cloudy",
      "windspeed": 12.3,
      "winddirection": 180.0,
      "time": "2024-01-14T12:00"
    },
    "forecast": [
      {
        "date": "2024-01-15",
        "max_temperature": 18.0,
        "min_temperature": 12.0,
        "condition": "Partly cloudy"
      }
    ]
  },
  "attractions": [
    {
      "name": "Eiffel Tower",
      "type": "attraction",
      "latitude": 48.8584,
      "longitude": 2.2945,
      "distance_km": 2.30,
      "description": null
    }
  ],
  "attraction_count": 5
}
```

## 🔧 API Details

### APIs Used

1. **Nominatim API** (Geocoding)
   - Converts place names to coordinates
   - Validates place existence
   - Base URL: `https://nominatim.openstreetmap.org/search`
   - Rate limit: 1 request per second (automatically handled)

2. **Open-Meteo API** (Weather)
   - Provides current weather and forecasts
   - Base URL: `https://api.open-meteo.com/v1/forecast`
   - Free, no API key required

3. **Overpass API** (Places)
   - Queries OpenStreetMap for tourist attractions
   - Base URL: `https://overpass-api.de/api/interpreter`
   - Finds attractions within 5km radius

## 🛠️ Project Structure

```
inkle/
├── src/
│   ├── agents/
│   │   ├── __init__.py
│   │   ├── tourism_agent.py      # Parent orchestrator agent
│   │   ├── weather_agent.py      # Weather child agent
│   │   └── places_agent.py       # Places child agent
│   ├── api_clients/
│   │   ├── __init__.py
│   │   ├── nominatim_client.py   # Geocoding API client
│   │   ├── openmeteo_client.py   # Weather API client
│   │   └── overpass_client.py    # Places API client
│   ├── models/
│   │   ├── __init__.py
│   │   ├── place.py              # Place data models
│   │   ├── weather.py             # Weather data models
│   │   └── attraction.py          # Attraction data models
│   └── utils/
│       ├── __init__.py
│       └── errors.py              # Custom exceptions
├── main.py                        # CLI entry point
├── requirements.txt               # Python dependencies
├── README.md                      # This file
└── PLAN.md                        # Implementation plan
```

## ⚠️ Error Handling

The system handles various error scenarios:

- **Non-existent places**: Returns user-friendly error message
- **API failures**: Gracefully handles network errors and API timeouts
- **Partial failures**: If one agent fails, others still provide data
- **Invalid responses**: Validates and handles malformed API responses

Example error response:
```
❌ Error: I don't know this place exists. Please check the spelling and try again.
Place: InvalidPlaceName
```

## 🧪 Testing

Test the system with various places:

```bash
# Major cities
python main.py "London"
python main.py "Tokyo"
python main.py "New York"

# Smaller places
python main.py "Barcelona"
python main.py "Sydney"

# Test error handling
python main.py "ThisPlaceDoesNotExist12345"
```

## 📝 Notes

- The system respects API rate limits (especially Nominatim's 1 req/sec policy)
- Overpass API queries may take 10-30 seconds for complex searches
- Some remote places may have limited attraction data
- Weather data is based on the nearest weather station

## 🔮 Future Enhancements

Potential improvements:
- Async/parallel execution of child agents
- Caching for frequently queried places
- Additional data sources (hotels, restaurants)
- Interactive mode with conversation
- Web interface
- More detailed attraction information

## 📄 License

This project is created for the Inkle Assignment: AI Intern.

## 👨‍💻 Author

Built as part of the Inkle AI Intern assignment.

---

**Enjoy exploring the world with AI! 🌍✨**

