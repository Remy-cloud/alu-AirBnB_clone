#!/usr/bin/python3
"""Defines unnittests for models/city.py."""
import unittest
from models.base_model import BaseModel
from models.city import City


class TestCity(unittest.TestCase):
    """Unittests for testing the City class."""

    def test_is_subclass(self):
        """Check that City is a subclass of BaseModel."""
        self.assertTrue(issubclass(City, BaseModel))

    def test_name(self):
        """Test that City has attr name, and it's an empty string"""
        city = City()
        self.assertTrue(hasattr(city, "name"))
        self.assertEqual(city.name, "")
        
        # Test name assignment
        city.name = "city name"
        self.assertEqual(city.name, "city name")

    def test_state_id(self):
        """Test that City has attr state_id, and it's an empty string"""
        city = City()
        self.assertTrue(hasattr(city, "state_id"))
        self.assertEqual(city.state_id, "")
        
        # Test state_id assignment
        city.state_id = "city state_id"
        self.assertEqual(city.state_id, "city state_id")




if __name__ == "__main__":
    unittest.main()