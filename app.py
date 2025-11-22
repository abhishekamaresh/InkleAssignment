#!/usr/bin/env python3
"""Flask web application for Tourism AI System."""

from flask import Flask, render_template, request, jsonify
from src.agents.tourism_agent import TourismAgent
from src.utils.errors import TourismSystemError
import json
import os

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False  # Support Unicode characters

# Initialize the tourism agent
tourism_agent = TourismAgent()


@app.route('/')
def index():
    """Render the main page."""
    return render_template('index.html')


@app.route('/api/search', methods=['POST'])
def search():
    """API endpoint to search for place information."""
    try:
        data = request.get_json()
        place_name = data.get('place', '').strip()
        
        if not place_name:
            return jsonify({
                'error': 'Place name is required',
                'success': False
            }), 400
        
        # Process the place
        response = tourism_agent.process(place_name)
        
        # Format response for frontend
        formatted_response = format_response_for_ui(response)
        
        return jsonify({
            'success': True,
            'data': formatted_response
        })
        
    except TourismSystemError as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500
    except Exception as e:
        return jsonify({
            'success': False,
            'error': f'Unexpected error: {str(e)}'
        }), 500


def format_response_for_ui(response):
    """Format the response for the UI."""
    if 'error' in response:
        return {
            'error': True,
            'message': response['error'],
            'place': response.get('place', '')
        }
    
    result = {
        'error': False,
        'place': response.get('place', {}),
        'weather': None,
        'attractions': []
    }
    
    # Format weather data
    if 'weather' in response:
        weather = response['weather']
        current = weather.get('current', {})
        forecast = weather.get('forecast', [])
        
        result['weather'] = {
            'current': {
                'temperature': round(current.get('temperature', 0), 1),
                'condition': current.get('condition', 'N/A'),
                'windspeed': round(current.get('windspeed', 0), 1) if current.get('windspeed') else None,
                'winddirection': current.get('winddirection'),
                'icon': get_weather_icon(current.get('condition', ''))
            },
            'forecast': [
                {
                    'date': day.get('date', ''),
                    'day_name': get_day_name(day.get('date', '')),
                    'max_temp': round(day.get('max_temperature', 0), 1),
                    'min_temp': round(day.get('min_temperature', 0), 1),
                    'condition': day.get('condition', 'N/A'),
                    'icon': get_weather_icon(day.get('condition', ''))
                }
                for day in forecast
            ]
        }
    
    # Format attractions
    if 'attractions' in response:
        result['attractions'] = [
            {
                'name': attr.get('name', 'Unknown'),
                'type': attr.get('type', 'attraction'),
                'distance': round(attr.get('distance_km', 0), 2) if attr.get('distance_km') else None,
                'icon': get_attraction_icon(attr.get('type', 'attraction')),
                'image_url': attr.get('image_url')
            }
            for attr in response['attractions']
        ]
    
    return result


def get_weather_icon(condition):
    """Get weather icon based on condition."""
    condition_lower = condition.lower()
    
    if 'clear' in condition_lower or 'sunny' in condition_lower:
        return '☀️'
    elif 'partly cloudy' in condition_lower or 'mainly clear' in condition_lower:
        return '⛅'
    elif 'cloudy' in condition_lower or 'overcast' in condition_lower:
        return '☁️'
    elif 'rain' in condition_lower or 'drizzle' in condition_lower or 'shower' in condition_lower:
        return '🌧️'
    elif 'snow' in condition_lower:
        return '❄️'
    elif 'thunder' in condition_lower or 'storm' in condition_lower:
        return '⛈️'
    elif 'fog' in condition_lower or 'mist' in condition_lower:
        return '🌫️'
    elif 'wind' in condition_lower:
        return '💨'
    else:
        return '🌤️'


def get_attraction_icon(attraction_type):
    """Get icon for attraction type."""
    type_lower = attraction_type.lower()
    
    if 'museum' in type_lower:
        return '🏛️'
    elif 'hotel' in type_lower or 'accommodation' in type_lower:
        return '🏨'
    elif 'monument' in type_lower or 'memorial' in type_lower:
        return '🗿'
    elif 'gallery' in type_lower or 'artwork' in type_lower:
        return '🖼️'
    elif 'zoo' in type_lower:
        return '🦁'
    elif 'theme_park' in type_lower:
        return '🎢'
    elif 'park' in type_lower or 'garden' in type_lower:
        return '🌳'
    elif 'viewpoint' in type_lower:
        return '👁️'
    elif 'theatre' in type_lower or 'cinema' in type_lower:
        return '🎭'
    elif 'historic' in type_lower:
        return '🏰'
    else:
        return '📍'


def get_day_name(date_str):
    """Get day name from date string."""
    try:
        from datetime import datetime
        date_obj = datetime.strptime(date_str, '%Y-%m-%d')
        days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        return days[date_obj.weekday()]
    except:
        return date_str


if __name__ == '__main__':
    # Get port from environment variable or default to 5001
    port = int(os.environ.get('PORT', 5001))
    # Only run in debug mode if explicitly set
    debug = os.environ.get('FLASK_DEBUG', 'False').lower() == 'true'
    app.run(debug=debug, host='0.0.0.0', port=port)

