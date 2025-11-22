#!/usr/bin/env python3
"""Quick test script to verify the system works."""

import sys
from src.agents.tourism_agent import TourismAgent
from src.utils.errors import TourismSystemError, PlaceNotFoundError


def test_system():
    """Test the tourism system with sample queries."""
    print("🧪 Testing Multi-Agent Tourism System\n")
    print("=" * 60)
    
    agent = TourismAgent()
    
    # Test cases
    test_cases = [
        ("Paris", "Valid major city"),
        ("Tokyo", "Valid major city"),
        ("InvalidPlaceName12345", "Non-existent place (should show error)"),
    ]
    
    for place_name, description in test_cases:
        print(f"\n📍 Test: {description}")
        print(f"   Place: {place_name}")
        print("-" * 60)
        
        try:
            response = agent.process(place_name)
            
            if "error" in response:
                print(f"   ✓ Error handling works: {response['error']}")
            else:
                place_info = response.get('place', {})
                weather = response.get('weather')
                attractions = response.get('attractions', [])
                
                print(f"   ✓ Place found: {place_info.get('display_name', 'N/A')}")
                if weather:
                    temp = weather.get('current', {}).get('temperature', 'N/A')
                    print(f"   ✓ Weather retrieved: {temp}°C")
                if attractions:
                    print(f"   ✓ Attractions found: {len(attractions)}")
                else:
                    print(f"   ⚠  No attractions found")
            
        except Exception as e:
            print(f"   ❌ Error: {str(e)}")
            import traceback
            traceback.print_exc()
    
    print("\n" + "=" * 60)
    print("✅ System test completed!")


if __name__ == "__main__":
    try:
        test_system()
    except KeyboardInterrupt:
        print("\n\n⚠️  Test interrupted by user.")
        sys.exit(130)
    except Exception as e:
        print(f"\n❌ Test failed: {str(e)}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

