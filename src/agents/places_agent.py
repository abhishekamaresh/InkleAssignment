"""Places Agent - Child Agent 2."""

from typing import List, Optional
from ..models.place import Coordinates
from ..models.attraction import Attraction
from ..api_clients.overpass_client import OverpassClient
from ..api_clients.image_client import ImageClient
from ..utils.errors import PlacesAPIError
from ..utils.famous_attractions import get_famous_attractions, calculate_distance


class PlacesAgent:
    """Agent responsible for finding tourist attractions."""
    
    def __init__(self, client: Optional[OverpassClient] = None, image_client: Optional[ImageClient] = None, max_attractions: int = 5):
        """Initialize Places Agent.
        
        Args:
            client: OverpassClient instance (creates new one if not provided)
            image_client: ImageClient instance (creates new one if not provided)
            max_attractions: Maximum number of attractions to return
        """
        self.client = client or OverpassClient()
        self.image_client = image_client or ImageClient()
        self.max_attractions = max_attractions
    
    def get_attractions(self, coordinates: Coordinates, place_name: Optional[str] = None) -> List[Attraction]:
        """Get tourist attractions near given coordinates.
        
        Args:
            coordinates: Geographic coordinates
            place_name: Name of the place (for famous attractions lookup)
            
        Returns:
            List of Attraction objects (up to max_attractions)
            
        Raises:
            PlacesAPIError: If attractions cannot be retrieved
        """
        try:
            # TOURIST GUIDE MODE: Always prioritize famous attractions
            famous_attrs = []
            if place_name:
                famous_data = get_famous_attractions(place_name, coordinates)
                for attr_data in famous_data:
                    distance = calculate_distance(
                        coordinates.latitude, coordinates.longitude,
                        attr_data['lat'], attr_data['lon']
                    )
                    famous_attrs.append(Attraction(
                        name=attr_data['name'],
                        attraction_type=attr_data['type'],
                        latitude=attr_data['lat'],
                        longitude=attr_data['lon'],
                        distance_km=distance
                    ))
            
            # If we have famous attractions, prioritize them
            if famous_attrs:
                # Sort famous attractions by priority (from database) and distance
                famous_attrs.sort(key=lambda x: (
                    x.distance_km if x.distance_km else float('inf')
                ))
                
                # Return famous attractions first (these are MUST-SEE landmarks)
                # Only get additional from Overpass if we need more
                if len(famous_attrs) >= self.max_attractions:
                    return famous_attrs[:self.max_attractions]
                
                # Get additional attractions from Overpass to fill remaining slots
                remaining_slots = self.max_attractions - len(famous_attrs)
                overpass_attrs = self.client.get_attractions(coordinates, limit=remaining_slots * 3)
                
                # Combine: famous first, then Overpass
                seen_names = {attr.name.lower() for attr in famous_attrs}
                all_attractions = list(famous_attrs)
                
                for attr in overpass_attrs:
                    if attr.name.lower() not in seen_names and len(all_attractions) < self.max_attractions:
                        all_attractions.append(attr)
                        seen_names.add(attr.name.lower())
                
                return all_attractions[:self.max_attractions]
            
            # If no famous attractions, fall back to Overpass API
            return self.client.get_attractions(coordinates, limit=self.max_attractions)
            
        except PlacesAPIError:
            raise
        except Exception as e:
            raise PlacesAPIError(f"Unexpected error in Places Agent: {str(e)}")
    
    def execute(self, coordinates: Coordinates, place_name: Optional[str] = None) -> List[dict]:
        """Execute agent task and return formatted result.
        
        Args:
            coordinates: Geographic coordinates
            place_name: Name of the place (for famous attractions lookup)
            
        Returns:
            List of dictionaries with attraction information
        """
        attractions = self.get_attractions(coordinates, place_name=place_name)
        
        # Add images to attractions
        for attraction in attractions:
            try:
                image_url = self.image_client.get_attraction_image(
                    attraction.name,
                    attraction.attraction_type
                )
                attraction.image_url = image_url
            except Exception:
                # If image fetch fails, continue without image
                pass
        
        return [attraction.to_dict() for attraction in attractions]

