"""Data models for the tourism system."""

from .place import Place, Coordinates
from .weather import Weather, CurrentWeather, ForecastDay
from .attraction import Attraction

__all__ = ['Place', 'Coordinates', 'Weather', 'CurrentWeather', 'ForecastDay', 'Attraction']

