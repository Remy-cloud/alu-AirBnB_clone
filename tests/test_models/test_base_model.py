#!/usr/bin/python3
"""Unittest for BaseModel class"""

import unittest
from models.base_model import BaseModel
from datetime import datetime
import time
import uuid


class TestBaseModel(unittest.TestCase):
    """Tests for BaseModel class"""

    def setUp(self):
        """Create a new BaseModel instance for each test"""
        self.model = BaseModel()

    def test_id_is_string(self):
        """Test if id is a string and is a valid UUID"""
        self.assertIsInstance(self.model.id, str)
        # Check if it's a valid UUID
        try:
            uuid_obj = uuid.UUID(self.model.id)
        except ValueError:
            self.fail("id is not a valid UUID string")

    def test_created_at_and_updated_at(self):
        """Test if created_at and updated_at are datetime objects"""
        self.assertIsInstance(self.model.created_at, datetime)
        self.assertIsInstance(self.model.updated_at, datetime)
        self.assertEqual(self.model.created_at, self.model.updated_at)

    def test_str_representation(self):
        """Test __str__ method output"""
        expected = f"[BaseModel] ({self.model.id}) {self.model.__dict__}"
        self.assertEqual(str(self.model), expected)

    def test_save_updates_updated_at(self):
        """Test if save() updates updated_at"""
        old_updated_at = self.model.updated_at
        time.sleep(0.1)  # Ensure time has passed
        self.model.save()
        self.assertGreater(self.model.updated_at, old_updated_at)

    def test_to_dict(self):
        """Test to_dict() returns a correct dictionary representation"""
        dict_repr = self.model.to_dict()
        self.assertEqual(dict_repr["__class__"], "BaseModel")
        self.assertEqual(dict_repr["id"], self.model.id)
        self.assertEqual(dict_repr["created_at"], self.model.created_at.isoformat())
        self.assertEqual(dict_repr["updated_at"], self.model.updated_at.isoformat())
        self.assertIsInstance(dict_repr, dict)


if __name__ == '__main__':
    unittest.main()
