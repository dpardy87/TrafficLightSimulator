"""
constants.py

This module defines global constants used by the Traffic Light Simulator.
"""

# List of the colors to be used
TRAFFIC_LIGHT_COLORS = ["RED", "YELLOW", "GREEN"]

# ANSI color codes
RED = "\033[31m"
YELLOW = "\033[33m"
GREEN = "\033[32m"
RESET = "\033[0m"

# Mapping of color names to ANSI codes
COLOR_MAP = {"RED": RED, "YELLOW": YELLOW, "GREEN": GREEN}

# Shared flag for stopping the simulation
STOP_SIMULATION = False
