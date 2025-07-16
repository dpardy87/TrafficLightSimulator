"""
Traffic Light Simulator

This program simulates a traditional three-color traffic light using terminal-based
ASCII art. Users are prompted to input the duration (in seconds) for each color,
and the simulation runs in a loop, cycling through RED, YELLOW, and GREEN lights.

Type 'exit' during the simulation to stop it gracefully.
"""

import os
import sys
import time
import threading
from constants import TRAFFIC_LIGHT_COLORS, RESET, COLOR_MAP, STOP_SIMULATION


class TrafficLight:
    """Represents a terminal-based traffic light simulator."""

    def __init__(self):
        """Initialize a new traffic light instance"""
        self.durations = {}

    @staticmethod
    def monitor_for_exit():
        """Waits for user to type 'exit' and sets flag to stop simulation."""
        global STOP_SIMULATION
        while True:
            if input().strip().lower() == "exit":
                STOP_SIMULATION = True
                print("Exiting Traffic Light Simulator")
                break

    @staticmethod
    def clear_screen():
        """Clear terminal"""
        os.system("cls" if os.name == "nt" else "clear")

    def get_duration_from_input(self, color):
        """Get duration of traffic light from user"""
        while True:
            user_input = (
                input(
                    f"Enter the duration (number of seconds) for the color of {color}: "
                )
                .strip()
                .lower()
            )
            if user_input == "exit":
                print("Exiting Traffic Light Simulator...")
                # exit program successfully
                sys.exit(0)
            try:
                duration = float(user_input)
                if duration > 0:
                    print(f"The duration for {color} is {duration} seconds.")
                    return duration
                print("Duration must be a positive number. Please try again.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")

    def set_durations_from_user(self):
        """Prompt the user to input durations for all traffic light colors."""
        for color in TRAFFIC_LIGHT_COLORS:
            self.durations[color] = self.get_duration_from_input(color)

    def generate_traffic_light_box(self, is_active, color_fg):
        """Return light box lines instead of printing."""
        fill = color_fg + "███████" + RESET if is_active else "       "
        return ["█████████", f"█{fill}█", f"█{fill}█", f"█{fill}█", "█████████"]

    def draw_full_traffic_light(self, active_color):
        """
        Draws the full traffic light with the active light fully colored.
        Parameters:
            active_color (str): One of 'RED', 'YELLOW', or 'GREEN'.
        """

        boxes = []  # Store all light box strings

        for color_name in TRAFFIC_LIGHT_COLORS:
            is_active = active_color == color_name
            color_code = COLOR_MAP[color_name]
            box_lines = self.generate_traffic_light_box(is_active, color_code)
            boxes.extend(box_lines)  # Add the 5 lines of the box

        # Print the full light
        print("\n".join(boxes))
        print(f"\n{active_color} light")

    def run(self):
        """Run the traffic light simulation based on stored durations."""
        while True:
            for color in TRAFFIC_LIGHT_COLORS:
                if STOP_SIMULATION:
                    sys.exit(0)
                self.clear_screen()
                self.draw_full_traffic_light(color)
                time.sleep(self.durations[color])


def main():
    """
    Entry point for Traffic Light Simulator.

    This function:
    - Welcomes the user and prompts for duration input for red, yellow, and green lights.
    - Starts a background thread to monitor for 'exit' command.
    - Runs the traffic light loop.
    - Handles graceful shutdown on keyboard interruption.
    """
    try:
        print("**Traffic Light Simulator, Databee.ai Candidate Evaluation**")
        print("You can type 'exit' at any time to quit.\n")

        traffic_light = TrafficLight()
        traffic_light.set_durations_from_user()

        # start a background thread to monitor user input for 'exit'
        threading.Thread(target=traffic_light.monitor_for_exit, daemon=True).start()

        # run the simulation loop
        traffic_light.run()

    except KeyboardInterrupt:
        print("\nExiting Traffic Light Simulator due to an interruption.")
        sys.exit(1)


if __name__ == "__main__":
    main()
