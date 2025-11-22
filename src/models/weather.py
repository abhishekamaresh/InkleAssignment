"""Weather data models."""

from dataclasses import dataclass
from typing import List, Optional
from datetime import datetime


@dataclass
class CurrentWeather:
    """Current weather information."""
    temperature: float
    condition: str
    windspeed: Optional[float] = None
    winddirection: Optional[float] = None
    time: Optional[str] = None
    
    def to_dict(self) -> dict:
        """Convert to dictionary."""
        return {
            'temperature': self.temperature,
            'condition': self.condition,
            'windspeed': self.windspeed,
            'winddirection': self.winddirection,
            'time': self.time
        }


@dataclass
class ForecastDay:
    """Forecast for a single day."""
    date: str
    max_temperature: float
    min_temperature: float
    condition: str
    
    def to_dict(self) -> dict:
        """Convert to dictionary."""
        return {
            'date': self.date,
            'max_temperature': self.max_temperature,
            'min_temperature': self.min_temperature,
            'condition': self.condition
        }


@dataclass
class Weather:
    """Complete weather information."""
    current: CurrentWeather
    forecast: List[ForecastDay]
    
    def to_dict(self) -> dict:
        """Convert to dictionary."""
        return {
            'current': self.current.to_dict(),
            'forecast': [day.to_dict() for day in self.forecast]
        }

