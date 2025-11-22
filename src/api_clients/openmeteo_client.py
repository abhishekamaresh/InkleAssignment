"""Open-Meteo API client for weather data."""

import requests
from typing import List
from datetime import datetime, timedelta
from ..models.weather import Weather, CurrentWeather, ForecastDay
from ..models.place import Coordinates
from ..utils.errors import WeatherAPIError


class OpenMeteoClient:
    """Client for Open-Meteo weather API."""
    
    BASE_URL = "https://api.open-meteo.com/v1/forecast"
    DEFAULT_TIMEOUT = 10
    FORECAST_DAYS = 7  # Show 7-day forecast for better weather app experience
    
    # Weather code to condition mapping (simplified)
    WEATHER_CODES = {
        0: "Clear sky",
        1: "Mainly clear",
        2: "Partly cloudy",
        3: "Overcast",
        45: "Foggy",
        48: "Depositing rime fog",
        51: "Light drizzle",
        53: "Moderate drizzle",
        55: "Dense drizzle",
        56: "Light freezing drizzle",
        57: "Dense freezing drizzle",
        61: "Slight rain",
        63: "Moderate rain",
        65: "Heavy rain",
        66: "Light freezing rain",
        67: "Heavy freezing rain",
        71: "Slight snow fall",
        73: "Moderate snow fall",
        75: "Heavy snow fall",
        77: "Snow grains",
        80: "Slight rain showers",
        81: "Moderate rain showers",
        82: "Violent rain showers",
        85: "Slight snow showers",
        86: "Heavy snow showers",
        95: "Thunderstorm",
        96: "Thunderstorm with slight hail",
        99: "Thunderstorm with heavy hail"
    }
    
    def __init__(self, timeout: int = DEFAULT_TIMEOUT, forecast_days: int = FORECAST_DAYS):
        """Initialize Open-Meteo client.
        
        Args:
            timeout: Request timeout in seconds
            forecast_days: Number of forecast days to retrieve
        """
        self.timeout = timeout
        self.forecast_days = forecast_days
    
    def _get_weather_condition(self, weather_code: int) -> str:
        """Convert weather code to human-readable condition.
        
        Args:
            weather_code: WMO weather code
            
        Returns:
            Human-readable weather condition
        """
        return self.WEATHER_CODES.get(weather_code, f"Weather code {weather_code}")
    
    def get_weather(self, coordinates: Coordinates) -> Weather:
        """Get current weather and forecast for coordinates.
        
        Args:
            coordinates: Geographic coordinates
            
        Returns:
            Weather object with current and forecast data
            
        Raises:
            WeatherAPIError: If API call fails
        """
        params = {
            'latitude': coordinates.latitude,
            'longitude': coordinates.longitude,
            'current_weather': 'true',
            'forecast_days': self.forecast_days,
            'timezone': 'auto',
            'daily': 'weathercode,temperature_2m_max,temperature_2m_min'
        }
        
        try:
            response = requests.get(
                self.BASE_URL,
                params=params,
                timeout=self.timeout
            )
            response.raise_for_status()
            
            data = response.json()
            
            # Parse current weather
            current_data = data.get('current_weather', {})
            current_weather = CurrentWeather(
                temperature=current_data.get('temperature', 0.0),
                condition=self._get_weather_condition(current_data.get('weathercode', 0)),
                windspeed=current_data.get('windspeed', None),
                winddirection=current_data.get('winddirection', None),
                time=current_data.get('time', None)
            )
            
            # Parse forecast
            daily_data = data.get('daily', {})
            forecast_days_list = []
            
            if daily_data:
                dates = daily_data.get('time', [])
                max_temps = daily_data.get('temperature_2m_max', [])
                min_temps = daily_data.get('temperature_2m_min', [])
                weather_codes = daily_data.get('weathercode', [])
                
                for i in range(min(len(dates), self.forecast_days)):
                    forecast_days_list.append(
                        ForecastDay(
                            date=dates[i],
                            max_temperature=max_temps[i] if i < len(max_temps) else 0.0,
                            min_temperature=min_temps[i] if i < len(min_temps) else 0.0,
                            condition=self._get_weather_condition(
                                weather_codes[i] if i < len(weather_codes) else 0
                            )
                        )
                    )
            
            return Weather(current=current_weather, forecast=forecast_days_list)
            
        except requests.exceptions.RequestException as e:
            raise WeatherAPIError(f"Failed to fetch weather data: {str(e)}")
        except (KeyError, ValueError, IndexError) as e:
            raise WeatherAPIError(f"Invalid response from weather API: {str(e)}")

