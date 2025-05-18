#!/usr/bin/env python3
"""
Simple HTTP server to serve the documentation.
"""

import http.server
import socketserver
import os
import sys
import webbrowser
from pathlib import Path

# Default port
PORT = 8000

def serve_docs():
    """Serve the documentation on localhost."""
    # Check if the build directory exists
    build_dir = Path(__file__).parent / "_build" / "html"
    if not build_dir.exists():
        print("Documentation not built yet. Building...")
        os.system("make html")
        if not build_dir.exists():
            print("Failed to build documentation.")
            sys.exit(1)
    
    # Change to the build directory
    os.chdir(build_dir)
    
    # Create the server
    handler = http.server.SimpleHTTPRequestHandler
    httpd = socketserver.TCPServer(("", PORT), handler)
    
    print(f"Serving documentation at http://localhost:{PORT}")
    print("Press Ctrl+C to stop the server.")
    
    # Open the browser
    webbrowser.open(f"http://localhost:{PORT}")
    
    # Start the server
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nServer stopped.")

if __name__ == "__main__":
    serve_docs()