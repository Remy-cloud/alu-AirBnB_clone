#!/usr/bin/env python3
"""FileStorage module: serializes and deserializes BaseModel instances to/from JSON file"""

import json
import os

class FileStorage:
    """Handles serialization and deserialization of BaseModel instances"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary of all stored objects"""
        return self.__objects

    def new(self, obj):
        """Adds a new object to storage dictionary"""
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file"""
        with open(self.__file_path, "w") as f:
            obj_dict = {k: v.to_dict() for k, v in self.__objects.items()}
            json.dump(obj_dict, f)

    def reload(self):
        """Deserializes the JSON file back to __objects"""
        from models.base_model import BaseModel
        try:
            with open(self.__file_path, "r") as f:
                obj_dict = json.load(f)
                for key, val in obj_dict.items():
                    class_name = val["__class__"]
                    if class_name == "BaseModel":
                        self.__objects[key] = BaseModel(**val)
        except FileNotFoundError:
            pass
