"""Tourism AI Agent - Parent Orchestrator Agent."""

import json
from typing import Dict, Any, Optional
from ..models.place import Place
from ..api_clients.nominatim_client import NominatimClient
from .weather_agent import WeatherAgent
from .places_agent import PlacesAgent
from ..utils.errors import (
    TourismSystemError,
    PlaceNotFoundError,
    WeatherAPIError,
    PlacesAPIError,
    GeocodingError
)


class TourismAgent:
    """Parent agent that orchestrates the tourism system."""
    
    def __init__(
        self,
        geocoding_client: Optional[NominatimClient] = None,
        weather_agent: Optional[WeatherAgent] = None,
        places_agent: Optional[PlacesAgent] = None
    ):
        """Initialize Tourism Agent.
        
        Args:
            geocoding_client: NominatimClient instance (creates new one if not provided)
            weather_agent: WeatherAgent instance (creates new one if not provided)
            places_agent: PlacesAgent instance (creates new one if not provided)
        """
        self.geocoding_client = geocoding_client or NominatimClient()
        self.weather_agent = weather_agent or WeatherAgent()
        self.places_agent = places_agent or PlacesAgent()
    
    def process(self, place_name: str) -> Dict[str, Any]:
        """Process a place name and return tourism information.
        
        This is the main orchestration method that:
        1. Geocodes the place name
        2. Fetches weather information
        3. Fetches tourist attractions
        4. Returns consolidated response
        
        Args:
            place_name: Name of the place to get information for
            
        Returns:
            Dictionary with place, weather, and attractions information
            
        Raises:
            PlaceNotFoundError: If place cannot be found
            TourismSystemError: For other system errors
        """
        # Step 1: Geocode the place
        try:
            place = self.geocoding_client.geocode(place_name)
        except PlaceNotFoundError:
            # Return user-friendly error message as specified
            return {
                "error": "I don't know this place exists. Please check the spelling and try again.",
                "place": place_name
            }
        except GeocodingError as e:
            raise TourismSystemError(f"Geocoding failed: {str(e)}")
        
        # Step 2 & 3: Fetch weather and attractions in parallel (conceptually)
        # In a real async implementation, these would run concurrently
        weather_data = None
        attractions_data = []
        
        weather_error = None
        places_error = None
        
        # Fetch weather
        try:
            weather_data = self.weather_agent.execute(place.coordinates)
        except WeatherAPIError as e:
            weather_error = str(e)
        
        # Fetch attractions - pass both original place_name and geocoded place.name for better matching
        # This ensures famous attractions are found even if geocoding returns a different name format
        try:
            # Try original place_name first, then fall back to geocoded name
            attractions_data = self.places_agent.execute(
                place.coordinates, 
                place_name=place_name  # Use original search term for better matching
            )
        except PlacesAPIError as e:
            places_error = str(e)
        
        # Build response
        response = {
            "place": {
                "name": place.name,
                "display_name": place.display_name or place.name,
                "country": place.country,
                "coordinates": {
                    "latitude": place.coordinates.latitude,
                    "longitude": place.coordinates.longitude
                }
            }
        }
        
        if weather_data:
            response["weather"] = weather_data
        elif weather_error:
            response["weather_error"] = weather_error
        
        if attractions_data:
            response["attractions"] = attractions_data
            response["attraction_count"] = len(attractions_data)
        elif places_error:
            response["places_error"] = places_error
        
        return response
    
    def format_response(self, response: Dict[str, Any], format_type: str = "json") -> str:
        """Format response for output.
        
        Args:
            response: Response dictionary
            format_type: Output format ('json' or 'text')
            
        Returns:
            Formatted string
        """
        if format_type == "json":
            return json.dumps(response, indent=2, ensure_ascii=False)
        elif format_type == "text":
            return self._format_text_response(response)
        else:
            return json.dumps(response, indent=2)
    
    def _format_text_response(self, response: Dict[str, Any]) -> str:
        """Format response as human-readable text.
        
        Args:
            response: Response dictionary
            
        Returns:
            Formatted text string
        """
        if "error" in response:
            return f"❌ Error: {response['error']}\nPlace: {response.get('place', 'Unknown')}"
        
        lines = []
        lines.append("=" * 60)
        lines.append(f"📍 {response['place']['display_name']}")
        if response['place'].get('country'):
            lines.append(f"   Country: {response['place']['country']}")
        lines.append(f"   Coordinates: {response['place']['coordinates']['latitude']:.4f}, "
                    f"{response['place']['coordinates']['longitude']:.4f}")
        lines.append("=" * 60)
        
        # Weather section
        if "weather" in response:
            weather = response["weather"]
            current = weather.get("current", {})
            lines.append("\n🌤️  CURRENT WEATHER")
            lines.append("-" * 60)
            lines.append(f"Temperature: {current.get('temperature', 'N/A')}°C")
            lines.append(f"Condition: {current.get('condition', 'N/A')}")
            if current.get('windspeed'):
                lines.append(f"Wind Speed: {current.get('windspeed')} km/h")
            
            forecast = weather.get("forecast", [])
            if forecast:
                lines.append("\n📅 FORECAST")
                lines.append("-" * 60)
                for day in forecast[:3]:  # Show next 3 days
                    lines.append(f"{day['date']}: {day['min_temperature']:.1f}°C - "
                               f"{day['max_temperature']:.1f}°C, {day['condition']}")
        elif "weather_error" in response:
            lines.append(f"\n⚠️  Weather: {response['weather_error']}")
        
        # Attractions section
        if "attractions" in response:
            attractions = response["attractions"]
            lines.append(f"\n🏛️  TOURIST ATTRACTIONS ({len(attractions)} found)")
            lines.append("-" * 60)
            for i, attr in enumerate(attractions, 1):
                distance = f" ({attr['distance_km']:.2f} km away)" if attr.get('distance_km') else ""
                lines.append(f"{i}. {attr['name']} ({attr['type']}){distance}")
        elif "places_error" in response:
            lines.append(f"\n⚠️  Attractions: {response['places_error']}")
        else:
            lines.append("\n🏛️  No tourist attractions found in the area.")
        
        lines.append("\n" + "=" * 60)
        return "\n".join(lines)

