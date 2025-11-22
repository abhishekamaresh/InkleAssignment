"""Place data models."""

from dataclasses import dataclass
from typing import Optional


@dataclass
class Coordinates:
    """Geographic coordinates."""
    latitude: float
    longitude: float
    
    def __str__(self) -> str:
        return f"({self.latitude}, {self.longitude})"


@dataclass
class Place:
    """Place information."""
    name: str
    coordinates: Coordinates
    display_name: Optional[str] = None
    country: Optional[str] = None
    
    def __str__(self) -> str:
        return self.display_name or self.name

