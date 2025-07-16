"""unit tests for traffic light class"""

import unittest
from unittest.mock import patch
import sys
import os

# Add parent directory
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from traffic_light_simulator import TrafficLight
from constants import TRAFFIC_LIGHT_COLORS


class TestTrafficLight(unittest.TestCase):
    """Unit tests for methods in the TrafficLight class."""

    def setUp(self):
        """Create a TrafficLight instance before each test."""
        self.traffic_light = TrafficLight()

    def test_generate_box_inactive(self):
        """
        Test that generate_traffic_light_box() returns a blank box when the light is inactive.
        """
        box = self.traffic_light.generate_traffic_light_box(False, "\033[31m")
        self.assertEqual(len(box), 5)
        self.assertIn("       ", box[1])

    @patch("builtins.input", side_effect=["5"])
    def test_get_duration_valid(self, mock_input):
        """
        Test that get_duration_from_input() returns a valid float when given a numeric input.
        """
        duration = self.traffic_light.get_duration_from_input("RED")
        self.assertEqual(duration, 5.0)

    @patch("builtins.input", side_effect=["exit"])
    def test_get_duration_exit(self, mock_input):
        """
        Test that get_duration_from_input() exits the program when 'exit' is entered.
        """
        with self.assertRaises(SystemExit):
            self.traffic_light.get_duration_from_input("RED")


if __name__ == "__main__":
    unittest.main()
