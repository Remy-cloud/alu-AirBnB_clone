#!/usr/bin/python3
"""BaseModel module for AirBnB clone project."""

import uuid
from datetime import datetime


class BaseModel:
    """
    base class for all airbnb clone models with 
    attributes 
    """

    def __init__(self, *args , **kwargs):
        """
        Initialize a new BaseModel instance.

        If kwargs is provided, it recreates an instance from a dictionary.
        Otherwise, it creates a new instance with a unique ID and timestamps.
        """

        if kwargs:
            for key, value in kwargs.items():
                if key =="created_at" or key == "updated_at":
                    value = datetime.fromisoformat(value)
                    if key != "__class__":
                        setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
    
    def __str__(self):
        """
        Return string representation of the BaseModel instance.
        Format: [<class name>] (<self.id>) <self.__dict__>
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        updated the "update_at" attribute with the current time and date
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        returns a dictionary representation of the instance
        """

        dict_rep = self.__dict__.copy()
        dict_rep["__class__"] = self.__class__.__name__
        dict_rep["created_at"] = self.created_at.isoformat()
        dict_rep["updated_at"] = self.updated_at.isoformat()
        return dict_rep
