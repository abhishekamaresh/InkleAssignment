#!/usr/bin/env python3
"""Example usage of the Tourism AI System."""

from src.agents.tourism_agent import TourismAgent


def main():
    """Demonstrate the tourism system."""
    print("🌍 Tourism AI System - Example Usage\n")
    print("=" * 70)
    
    # Initialize the agent
    agent = TourismAgent()
    
    # Example places to query
    places = [
        "Paris",
        "Tokyo",
        "New York"
    ]
    
    for place_name in places:
        print(f"\n{'='*70}")
        print(f"Querying: {place_name}")
        print("="*70)
        
        try:
            # Process the place
            response = agent.process(place_name)
            
            # Format as text for display
            output = agent.format_response(response, format_type="text")
            print(output)
            
        except Exception as e:
            print(f"❌ Error processing {place_name}: {str(e)}")
        
        print("\n")
    
    # Test error handling
    print("="*70)
    print("Testing Error Handling: Non-existent place")
    print("="*70)
    
    try:
        response = agent.process("ThisPlaceDoesNotExist12345")
        output = agent.format_response(response, format_type="text")
        print(output)
    except Exception as e:
        print(f"❌ Error: {str(e)}")
    
    print("\n" + "="*70)
    print("✅ Examples completed!")
    print("="*70)


if __name__ == "__main__":
    main()

