"""Overpass API client for tourist attractions."""

import requests
import math
from typing import List
from ..models.attraction import Attraction
from ..models.place import Coordinates
from ..utils.errors import PlacesAPIError


class OverpassClient:
    """Client for Overpass API to find tourist attractions."""
    
    BASE_URL = "https://overpass-api.de/api/interpreter"
    DEFAULT_TIMEOUT = 30  # Overpass can be slow
    SEARCH_RADIUS = 10000  # 10km radius in meters (increased for more attractions)
    MAX_RESULTS = 20  # Get more than needed, then filter to top results
    
    def __init__(self, timeout: int = DEFAULT_TIMEOUT, search_radius: int = SEARCH_RADIUS):
        """Initialize Overpass client.
        
        Args:
            timeout: Request timeout in seconds
            search_radius: Search radius in meters
        """
        self.timeout = timeout
        self.search_radius = search_radius
    
    def _calculate_distance(self, lat1: float, lon1: float, lat2: float, lon2: float) -> float:
        """Calculate distance between two coordinates in kilometers using Haversine formula.
        
        Args:
            lat1, lon1: First point coordinates
            lat2, lon2: Second point coordinates
            
        Returns:
            Distance in kilometers
        """
        R = 6371  # Earth radius in kilometers
        
        dlat = math.radians(lat2 - lat1)
        dlon = math.radians(lon2 - lon1)
        
        a = (math.sin(dlat / 2) ** 2 +
             math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) *
             math.sin(dlon / 2) ** 2)
        c = 2 * math.asin(math.sqrt(a))
        
        return R * c
    
    def _build_query(self, coordinates: Coordinates) -> str:
        """Build Overpass QL query for tourist attractions.
        
        Args:
            coordinates: Center point for search
            
        Returns:
            Overpass QL query string
        """
        # Enhanced query to get more diverse attractions
        # Includes historical sites, landmarks, parks, and more
        query = f"""[out:json][timeout:30];
(
  // Tourism features
  node["tourism"~"^(attraction|museum|gallery|zoo|theme_park|viewpoint|monument|memorial|artwork|information|hostel|guest_house)$"](around:{self.search_radius},{coordinates.latitude},{coordinates.longitude});
  way["tourism"~"^(attraction|museum|gallery|zoo|theme_park|viewpoint|monument|memorial|artwork|information|hostel|guest_house)$"](around:{self.search_radius},{coordinates.latitude},{coordinates.longitude});
  relation["tourism"~"^(attraction|museum|gallery|zoo|theme_park|viewpoint|monument|memorial|artwork|information|hostel|guest_house)$"](around:{self.search_radius},{coordinates.latitude},{coordinates.longitude});
  // Historical sites
  node["historic"](around:{self.search_radius},{coordinates.latitude},{coordinates.longitude});
  way["historic"](around:{self.search_radius},{coordinates.latitude},{coordinates.longitude});
  relation["historic"](around:{self.search_radius},{coordinates.latitude},{coordinates.longitude});
  // Landmarks and notable places
  node["amenity"~"^(theatre|cinema|arts_centre|community_centre)$"](around:{self.search_radius},{coordinates.latitude},{coordinates.longitude});
  way["amenity"~"^(theatre|cinema|arts_centre|community_centre)$"](around:{self.search_radius},{coordinates.latitude},{coordinates.longitude});
  // Parks and gardens
  node["leisure"~"^(park|garden|nature_reserve)$"](around:{self.search_radius},{coordinates.latitude},{coordinates.longitude});
  way["leisure"~"^(park|garden|nature_reserve)$"](around:{self.search_radius},{coordinates.latitude},{coordinates.longitude});
);
out center tags;"""
        return query
    
    def get_attractions(self, coordinates: Coordinates, limit: int = 5) -> List[Attraction]:
        """Get tourist attractions near coordinates.
        
        Args:
            coordinates: Center point for search
            limit: Maximum number of attractions to return
            
        Returns:
            List of Attraction objects (up to limit)
            
        Raises:
            PlacesAPIError: If API call fails
        """
        query = self._build_query(coordinates)
        
        try:
            response = requests.post(
                self.BASE_URL,
                data=query,
                headers={'Content-Type': 'text/plain'},
                timeout=self.timeout
            )
            response.raise_for_status()
            
            data = response.json()
            elements = data.get('elements', [])
            
            if not elements:
                return []
            
            attractions = []
            seen_names = set()  # Avoid duplicates
            
            for element in elements[:self.MAX_RESULTS * 2]:  # Process more to filter better
                tags = element.get('tags', {})
                name = tags.get('name') or tags.get('name:en') or tags.get('name:en') or 'Unnamed Attraction'
                
                # Skip if we've seen this name before
                if name.lower() in seen_names:
                    continue
                seen_names.add(name.lower())
                
                # Determine type - prioritize tourism, then historic, then amenity, then leisure
                tourism_type = tags.get('tourism') or tags.get('historic') or tags.get('amenity') or tags.get('leisure') or 'attraction'
                
                # Normalize type names
                if tourism_type in ['theatre', 'cinema', 'arts_centre']:
                    tourism_type = 'theatre'
                elif tourism_type in ['park', 'garden', 'nature_reserve']:
                    tourism_type = 'park'
                elif tourism_type in ['hostel', 'guest_house']:
                    tourism_type = 'accommodation'
                
                # Get coordinates
                if 'lat' in element and 'lon' in element:
                    lat = element['lat']
                    lon = element['lon']
                elif 'center' in element:
                    lat = element['center'].get('lat')
                    lon = element['center'].get('lon')
                else:
                    continue  # Skip if no coordinates
                
                # Calculate distance
                distance = self._calculate_distance(
                    coordinates.latitude, coordinates.longitude,
                    lat, lon
                )
                
                # Get description if available
                description = tags.get('description') or tags.get('description:en') or tags.get('wikipedia') or ''
                
                # Skip unnamed or very generic attractions
                if name.lower() in ['unnamed attraction', 'attraction', '']:
                    continue
                
                attractions.append(
                    Attraction(
                        name=name,
                        attraction_type=tourism_type,
                        latitude=lat,
                        longitude=lon,
                        distance_km=distance,
                        description=description
                    )
                )
            
            # Sort by distance and return top results
            attractions.sort(key=lambda x: x.distance_km if x.distance_km else float('inf'))
            
            # Prioritize diverse types - try to get different types of attractions
            if len(attractions) > limit:
                diverse_attractions = []
                seen_types = set()
                
                # First pass: get one of each type
                for attr in attractions:
                    if attr.attraction_type not in seen_types:
                        diverse_attractions.append(attr)
                        seen_types.add(attr.attraction_type)
                        if len(diverse_attractions) >= limit:
                            break
                
                # Second pass: fill remaining slots
                for attr in attractions:
                    if attr not in diverse_attractions and len(diverse_attractions) < limit:
                        diverse_attractions.append(attr)
                
                return diverse_attractions[:limit]
            
            return attractions[:limit]
            
        except requests.exceptions.RequestException as e:
            raise PlacesAPIError(f"Failed to fetch attractions: {str(e)}")
        except (KeyError, ValueError, IndexError) as e:
            raise PlacesAPIError(f"Invalid response from places API: {str(e)}")

