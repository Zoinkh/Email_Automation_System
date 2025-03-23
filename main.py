import sys
import os
import Lib
# Get the absolute path to the 'other_file' directory
lib = os.path.join(os.path.dirname(__file__), "Lib")

# Add the 'other_file' directory to sys.path
sys.path.append(lib)

# Now you can import from other_file.py

# Use the functions
Lib.menu.Menu()