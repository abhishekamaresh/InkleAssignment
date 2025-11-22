"""Attraction data models."""

from dataclasses import dataclass
from typing import Optional


@dataclass
class Attraction:
    """Tourist attraction information."""
    name: str
    attraction_type: str
    latitude: Optional[float] = None
    longitude: Optional[float] = None
    distance_km: Optional[float] = None
    description: Optional[str] = None
    image_url: Optional[str] = None
    
    def to_dict(self) -> dict:
        """Convert to dictionary."""
        return {
            'name': self.name,
            'type': self.attraction_type,
            'latitude': self.latitude,
            'longitude': self.longitude,
            'distance_km': round(self.distance_km, 2) if self.distance_km else None,
            'description': self.description,
            'image_url': self.image_url
        }
    
    def __str__(self) -> str:
        distance_str = f" ({self.distance_km:.2f} km away)" if self.distance_km else ""
        return f"{self.name} ({self.attraction_type}){distance_str}"

