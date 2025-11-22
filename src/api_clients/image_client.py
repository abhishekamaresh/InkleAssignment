"""Image API client for fetching attraction images."""

import requests
from typing import Optional
from ..utils.errors import APIError


class ImageClient:
    """Client for fetching images from Unsplash API."""
    
    # Using Unsplash Source API (no key required for basic usage)
    UNSPLASH_SOURCE = "https://source.unsplash.com"
    UNSPLASH_API = "https://api.unsplash.com"
    
    # Fallback to a placeholder service
    PLACEHOLDER_API = "https://picsum.photos"
    
    def __init__(self, use_unsplash_api: bool = False, api_key: Optional[str] = None):
        """Initialize Image Client.
        
        Args:
            use_unsplash_api: Whether to use Unsplash API (requires key) or Source API
            api_key: Unsplash API key (optional, uses Source API if not provided)
        """
        self.use_unsplash_api = use_unsplash_api and api_key
        self.api_key = api_key
    
    def get_attraction_image(self, attraction_name: str, attraction_type: str, width: int = 400, height: int = 300) -> str:
        """Get image URL for an attraction.
        
        Args:
            attraction_name: Name of the attraction
            attraction_type: Type of attraction
            width: Image width
            height: Image height
            
        Returns:
            Image URL
        """
        # Build search query
        search_terms = self._build_search_query(attraction_name, attraction_type)
        
        if self.use_unsplash_api and self.api_key:
            return self._get_unsplash_api_image(search_terms, width, height)
        else:
            # Use Unsplash Source API (no key needed, but less reliable)
            return self._get_unsplash_source_image(search_terms, width, height)
    
    def _build_search_query(self, name: str, attraction_type: str) -> str:
        """Build search query for image search.
        
        Args:
            name: Attraction name
            attraction_type: Type of attraction
            
        Returns:
            Search query string
        """
        # Clean the name
        clean_name = name.split(',')[0].strip()  # Take first part before comma
        
        # Build query based on type
        type_mapping = {
            'museum': 'museum',
            'gallery': 'art gallery',
            'monument': 'monument',
            'memorial': 'memorial',
            'hotel': 'hotel',
            'zoo': 'zoo',
            'theme_park': 'theme park',
            'viewpoint': 'viewpoint',
            'artwork': 'artwork',
            'attraction': 'tourist attraction'
        }
        
        type_query = type_mapping.get(attraction_type.lower(), 'landmark')
        
        # Combine name and type
        query = f"{clean_name} {type_query}"
        return query.replace(' ', '+')
    
    def _get_unsplash_source_image(self, query: str, width: int, height: int) -> str:
        """Get image from Unsplash Source API.
        
        Args:
            query: Search query
            width: Image width
            height: Image height
            
        Returns:
            Image URL
        """
        # Unsplash Source API format
        return f"{self.UNSPLASH_SOURCE}/{width}x{height}/?{query}"
    
    def _get_unsplash_api_image(self, query: str, width: int, height: int) -> str:
        """Get image from Unsplash API (requires API key).
        
        Args:
            query: Search query
            width: Image width
            height: Image height
            
        Returns:
            Image URL
        """
        try:
            url = f"{self.UNSPLASH_API}/search/photos"
            params = {
                'query': query.replace('+', ' '),
                'per_page': 1,
                'client_id': self.api_key
            }
            
            response = requests.get(url, params=params, timeout=5)
            response.raise_for_status()
            
            data = response.json()
            if data.get('results') and len(data['results']) > 0:
                return data['results'][0]['urls']['regular']
            
            # Fallback to placeholder
            return self._get_placeholder_image(width, height)
            
        except Exception:
            return self._get_placeholder_image(width, height)
    
    def _get_placeholder_image(self, width: int, height: int) -> str:
        """Get placeholder image.
        
        Args:
            width: Image width
            height: Image height
            
        Returns:
            Placeholder image URL
        """
        # Use Picsum Photos as fallback
        return f"{self.PLACEHOLDER_API}/{width}/{height}?random"
    
    def get_city_image(self, city_name: str, width: int = 1200, height: int = 600) -> str:
        """Get image for a city.
        
        Args:
            city_name: Name of the city
            width: Image width
            height: Image height
            
        Returns:
            Image URL
        """
        query = city_name.replace(' ', '+')
        return f"{self.UNSPLASH_SOURCE}/{width}x{height}/?{query},city"

