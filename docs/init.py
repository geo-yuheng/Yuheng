#!/usr/bin/env python3
"""
Documentation setup script.
This script installs the required dependencies for building the documentation.
"""

import subprocess
import sys

def install_dependencies():
    """Install the required dependencies for building the documentation."""
    dependencies = [
        "sphinx",
        "furo",
        "sphinx-autodoc-typehints",
        "sphinx-copybutton",
        "myst-parser"
    ]
    
    print("Installing documentation dependencies...")
    for dep in dependencies:
        print(f"Installing {dep}...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", dep])
    
    print("All dependencies installed successfully!")

if __name__ == "__main__":
    install_dependencies()