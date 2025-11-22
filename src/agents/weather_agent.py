"""Weather Agent - Child Agent 1."""

from typing import Optional
from ..models.place import Coordinates
from ..models.weather import Weather
from ..api_clients.openmeteo_client import OpenMeteoClient
from ..utils.errors import WeatherAPIError


class WeatherAgent:
    """Agent responsible for fetching weather information."""
    
    def __init__(self, client: Optional[OpenMeteoClient] = None):
        """Initialize Weather Agent.
        
        Args:
            client: OpenMeteoClient instance (creates new one if not provided)
        """
        self.client = client or OpenMeteoClient()
    
    def get_weather(self, coordinates: Coordinates) -> Weather:
        """Get weather information for given coordinates.
        
        Args:
            coordinates: Geographic coordinates
            
        Returns:
            Weather object with current and forecast data
            
        Raises:
            WeatherAPIError: If weather data cannot be retrieved
        """
        try:
            return self.client.get_weather(coordinates)
        except WeatherAPIError:
            raise
        except Exception as e:
            raise WeatherAPIError(f"Unexpected error in Weather Agent: {str(e)}")
    
    def execute(self, coordinates: Coordinates) -> dict:
        """Execute agent task and return formatted result.
        
        Args:
            coordinates: Geographic coordinates
            
        Returns:
            Dictionary with weather information
        """
        weather = self.get_weather(coordinates)
        return weather.to_dict()

