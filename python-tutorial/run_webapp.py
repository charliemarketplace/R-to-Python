#!/usr/bin/env python
"""Run the Python Tutorial web GUI."""

import argparse
import webbrowser
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description="Python Tutorial Web GUI")
    parser.add_argument('--port', type=int, default=5000, help='Port to run on (default: 5000)')
    parser.add_argument('--no-browser', action='store_true', help='Do not open browser automatically')
    parser.add_argument('--debug', action='store_true', help='Run in debug mode')
    args = parser.parse_args()

    # Import here to avoid slow startup for --help
    from src.webapp.app import create_app

    project_root = Path(__file__).parent
    app = create_app(project_root)

    url = f"http://127.0.0.1:{args.port}"

    print(f"\n  Python Tutorial Web GUI")
    print(f"  Running at: {url}")
    print(f"  Press Ctrl+C to stop\n")

    if not args.no_browser:
        webbrowser.open(url)

    app.run(host='127.0.0.1', port=args.port, debug=args.debug)


if __name__ == '__main__':
    main()
