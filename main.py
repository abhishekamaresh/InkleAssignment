#!/usr/bin/env python3
"""Main entry point for the Tourism AI System."""

import sys
import argparse
from src.agents.tourism_agent import TourismAgent
from src.utils.errors import TourismSystemError


def main():
    """Main CLI entry point."""
    parser = argparse.ArgumentParser(
        description="Multi-Agent Tourism System - Get weather and attractions for any place",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python main.py "Paris"
  python main.py "Tokyo" --format text
  python main.py "New York" --format json
        """
    )
    
    parser.add_argument(
        'place',
        type=str,
        help='Name of the place to get information for'
    )
    
    parser.add_argument(
        '--format',
        choices=['json', 'text'],
        default='text',
        help='Output format (default: text)'
    )
    
    args = parser.parse_args()
    
    # Initialize the tourism agent
    agent = TourismAgent()
    
    try:
        # Process the place
        response = agent.process(args.place)
        
        # Format and print response
        output = agent.format_response(response, format_type=args.format)
        print(output)
        
        # Exit with error code if there's an error in response
        if "error" in response:
            sys.exit(1)
        
    except TourismSystemError as e:
        print(f"❌ System Error: {str(e)}", file=sys.stderr)
        sys.exit(1)
    except KeyboardInterrupt:
        print("\n\n⚠️  Operation cancelled by user.", file=sys.stderr)
        sys.exit(130)
    except Exception as e:
        print(f"❌ Unexpected error: {str(e)}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()

