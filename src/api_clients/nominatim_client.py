"""Nominatim API client for geocoding."""

import time
import requests
from typing import Optional
from ..models.place import Place, Coordinates
from ..utils.errors import GeocodingError, PlaceNotFoundError


class NominatimClient:
    """Client for Nominatim geocoding API."""
    
    BASE_URL = "https://nominatim.openstreetmap.org/search"
    DEFAULT_TIMEOUT = 10
    RATE_LIMIT_DELAY = 1.0  # Nominatim requires 1 second between requests
    
    def __init__(self, timeout: int = DEFAULT_TIMEOUT, rate_limit_delay: float = RATE_LIMIT_DELAY):
        """Initialize Nominatim client.
        
        Args:
            timeout: Request timeout in seconds
            rate_limit_delay: Delay between requests in seconds (Nominatim policy)
        """
        self.timeout = timeout
        self.rate_limit_delay = rate_limit_delay
        self.last_request_time = 0.0
    
    def _wait_for_rate_limit(self):
        """Wait if necessary to respect rate limits."""
        current_time = time.time()
        time_since_last_request = current_time - self.last_request_time
        if time_since_last_request < self.rate_limit_delay:
            time.sleep(self.rate_limit_delay - time_since_last_request)
        self.last_request_time = time.time()
    
    def geocode(self, place_name: str) -> Place:
        """Geocode a place name to coordinates.
        
        Args:
            place_name: Name of the place to geocode
            
        Returns:
            Place object with coordinates and metadata
            
        Raises:
            PlaceNotFoundError: If place cannot be found
            GeocodingError: If API call fails
        """
        if not place_name or not place_name.strip():
            raise PlaceNotFoundError("Place name cannot be empty")
        
        self._wait_for_rate_limit()
        
        params = {
            'q': place_name.strip(),
            'format': 'json',
            'limit': 1,
            'addressdetails': 1
        }
        
        headers = {
            'User-Agent': 'Tourism-AI-System/1.0'  # Nominatim requires User-Agent
        }
        
        try:
            response = requests.get(
                self.BASE_URL,
                params=params,
                headers=headers,
                timeout=self.timeout
            )
            response.raise_for_status()
            
            data = response.json()
            
            if not data or len(data) == 0:
                raise PlaceNotFoundError(
                    f"I don't know this place exists. Please check the spelling and try again."
                )
            
            result = data[0]
            lat = float(result['lat'])
            lon = float(result['lon'])
            
            # Extract additional information
            address = result.get('address', {})
            display_name = result.get('display_name', place_name)
            country = address.get('country', None)
            
            return Place(
                name=place_name,
                coordinates=Coordinates(latitude=lat, longitude=lon),
                display_name=display_name,
                country=country
            )
            
        except requests.exceptions.RequestException as e:
            raise GeocodingError(f"Failed to geocode place '{place_name}': {str(e)}")
        except (KeyError, ValueError, IndexError) as e:
            raise GeocodingError(f"Invalid response from geocoding API: {str(e)}")

