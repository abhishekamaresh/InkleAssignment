# Multi-Agent Tourism System - Implementation Plan

## Overview
Build a multi-agent tourism system that provides weather information and tourist attraction suggestions for a given place.

## System Architecture

### High-Level Design
```
User Input (Place Name)
    ↓
Tourism AI Agent (Parent/Orchestrator)
    ├──→ Nominatim API (Geocoding: Place → Coordinates)
    ├──→ Weather Agent (Child Agent 1)
    │   └──→ Open-Meteo API (Weather Data)
    └──→ Places Agent (Child Agent 2)
        └──→ Overpass API (Tourist Attractions)
    ↓
Consolidated Response (Weather + Attractions)
```

## Components Breakdown

### 1. Parent Agent: Tourism AI Agent
**Responsibilities:**
- Receive user input (place name)
- Validate place existence using Nominatim API
- Orchestrate child agents (Weather & Places)
- Handle errors for non-existent places
- Aggregate and format responses from child agents
- Return final consolidated response

**Key Features:**
- Input validation
- Error handling and user-friendly error messages
- Coordination between child agents
- Response formatting

### 2. Child Agent 1: Weather Agent
**Responsibilities:**
- Accept coordinates (lat, lon) from parent agent
- Query Open-Meteo API for current and forecast weather
- Parse and format weather data
- Return structured weather information

**API Details:**
- **Endpoint:** `https://api.open-meteo.com/v1/forecast`
- **Parameters:** latitude, longitude, current_weather, forecast_days
- **Documentation:** https://open-meteo.com/en/docs

**Data to Extract:**
- Current temperature
- Weather condition
- Forecast (next few days)

### 3. Child Agent 2: Places Agent
**Responsibilities:**
- Accept coordinates (lat, lon) from parent agent
- Query Overpass API for tourist attractions
- Filter and rank attractions
- Return up to 5 tourist attractions

**API Details:**
- **Base URL:** `https://overpass-api.de/api/interpreter`
- **Query Type:** Overpass QL to find tourist attractions (tourism=attraction, tourism=hotel, etc.)
- **Documentation:** https://wiki.openstreetmap.org/wiki/Overpass_API

**Data to Extract:**
- Attraction name
- Type/category
- Location details
- Coordinates (optional)

### 4. Geocoding Service: Nominatim API
**Responsibilities:**
- Convert place name to coordinates
- Validate place existence
- Return lat/lon for API calls

**API Details:**
- **Base URL:** `https://nominatim.openstreetmap.org/search`
- **Parameters:** q (query), format=json, limit=1
- **Documentation:** https://nominatim.org/release-docs/develop/api/Search/

## Technology Stack Options

### Option 1: Python with LangChain/LangGraph (Recommended)
**Pros:**
- Built-in multi-agent orchestration
- Easy API integration
- Good error handling
- Clean agent abstraction

**Libraries:**
- `langchain` or `langgraph` - Agent framework
- `requests` or `httpx` - API calls
- `pydantic` - Data validation
- `python-dotenv` - Environment variables

### Option 2: Python with Custom Agent Framework
**Pros:**
- Full control over implementation
- Lightweight
- Easy to understand

**Libraries:**
- `requests` - API calls
- `dataclasses` or `pydantic` - Data models
- Custom agent classes

### Option 3: Node.js/TypeScript
**Pros:**
- Good for web integration
- Async/await support

**Libraries:**
- `axios` or `fetch` - API calls
- TypeScript for type safety

## Implementation Steps

### Phase 1: Setup & Infrastructure
1. **Project Setup**
   - Initialize project structure
   - Set up dependency management (requirements.txt or package.json)
   - Create configuration files
   - Set up environment variables if needed

2. **API Integration Layer**
   - Create API client classes/modules:
     - `NominatimClient` - Geocoding
     - `OpenMeteoClient` - Weather data
     - `OverpassClient` - Places data
   - Implement error handling for API calls
   - Add retry logic and rate limiting considerations

### Phase 2: Agent Implementation
1. **Geocoding Service**
   - Implement place name → coordinates conversion
   - Add validation for non-existent places
   - Return structured error if place not found

2. **Weather Agent**
   - Implement agent class with coordinate input
   - Integrate Open-Meteo API
   - Parse and format weather response
   - Handle API errors gracefully

3. **Places Agent**
   - Implement agent class with coordinate input
   - Construct Overpass QL queries for tourist attractions
   - Filter and limit to top 5 attractions
   - Format response with attraction details

4. **Parent Tourism Agent**
   - Implement orchestration logic
   - Coordinate geocoding → child agents flow
   - Aggregate responses from child agents
   - Format final output

### Phase 3: Error Handling & Edge Cases
1. **Non-existent Places**
   - Detect when Nominatim returns no results
   - Return user-friendly error message
   - Prevent child agents from executing

2. **API Failures**
   - Handle network errors
   - Handle API rate limits
   - Partial failures (one agent fails, other succeeds)
   - Timeout handling

3. **Data Validation**
   - Validate coordinates
   - Validate API responses
   - Handle missing data fields

### Phase 4: Testing & Refinement
1. **Unit Tests**
   - Test each agent independently
   - Test API clients
   - Test error handling

2. **Integration Tests**
   - Test full flow with real APIs
   - Test with various place names
   - Test error scenarios

3. **Edge Cases**
   - Places with no attractions
   - Places with weather data unavailable
   - Special characters in place names
   - International place names

## Project Structure

```
inkle/
├── src/
│   ├── agents/
│   │   ├── __init__.py
│   │   ├── tourism_agent.py      # Parent agent
│   │   ├── weather_agent.py      # Child agent 1
│   │   └── places_agent.py       # Child agent 2
│   ├── api_clients/
│   │   ├── __init__.py
│   │   ├── nominatim_client.py   # Geocoding
│   │   ├── openmeteo_client.py   # Weather API
│   │   └── overpass_client.py    # Places API
│   ├── models/
│   │   ├── __init__.py
│   │   ├── place.py              # Place data model
│   │   ├── weather.py             # Weather data model
│   │   └── attraction.py          # Attraction data model
│   └── utils/
│       ├── __init__.py
│       └── errors.py              # Custom exceptions
├── tests/
│   ├── test_agents.py
│   ├── test_api_clients.py
│   └── test_integration.py
├── main.py                        # Entry point
├── requirements.txt
├── README.md
└── PLAN.md                        # This file
```

## API Query Examples

### Nominatim API
```
GET https://nominatim.openstreetmap.org/search?q=Paris&format=json&limit=1
```

### Open-Meteo API
```
GET https://api.open-meteo.com/v1/forecast?latitude=48.8566&longitude=2.3522&current_weather=true&forecast_days=3
```

### Overpass API
```
POST https://overpass-api.de/api/interpreter
Body: [out:json];
(
  node["tourism"~"^(attraction|hotel|museum)$"](around:5000,48.8566,2.3522);
  way["tourism"~"^(attraction|hotel|museum)$"](around:5000,48.8566,2.3522);
);
out center;
```

## Response Format

### Success Response
```json
{
  "place": "Paris, France",
  "coordinates": {
    "latitude": 48.8566,
    "longitude": 2.3522
  },
  "weather": {
    "current": {
      "temperature": 15.5,
      "condition": "Partly cloudy",
      "windspeed": 12.3
    },
    "forecast": [...]
  },
  "attractions": [
    {
      "name": "Eiffel Tower",
      "type": "attraction",
      "distance": "2.3 km"
    },
    ...
  ]
}
```

### Error Response (Non-existent Place)
```json
{
  "error": "I don't know this place exists. Please check the spelling and try again.",
  "place": "InvalidPlaceName"
}
```

## Next Steps

1. **Choose Technology Stack** - Recommend Python with custom agent framework for simplicity
2. **Set up project structure** - Create directories and base files
3. **Implement API clients** - Start with Nominatim, then Weather, then Places
4. **Implement agents** - Start with child agents, then parent agent
5. **Add error handling** - Implement comprehensive error handling
6. **Create CLI/Interface** - Simple command-line interface for testing
7. **Test thoroughly** - Test with various places and edge cases
8. **Documentation** - Create README with usage examples

## Considerations

1. **Rate Limiting**: Nominatim has usage policies - may need to add delays
2. **API Reliability**: Implement retries and fallbacks
3. **Response Time**: Consider parallel execution of child agents
4. **Data Quality**: Filter and validate attraction data from Overpass
5. **User Experience**: Provide clear, formatted output
6. **Extensibility**: Design for easy addition of more child agents

