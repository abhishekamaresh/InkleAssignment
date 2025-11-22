"""Custom exceptions for the tourism system."""


class TourismSystemError(Exception):
    """Base exception for tourism system errors."""
    pass


class PlaceNotFoundError(TourismSystemError):
    """Raised when a place cannot be found."""
    pass


class APIError(TourismSystemError):
    """Raised when an API call fails."""
    pass


class WeatherAPIError(APIError):
    """Raised when weather API call fails."""
    pass


class PlacesAPIError(APIError):
    """Raised when places API call fails."""
    pass


class GeocodingError(APIError):
    """Raised when geocoding API call fails."""
    pass

