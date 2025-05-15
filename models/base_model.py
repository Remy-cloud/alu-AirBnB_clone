#!/usr/bin/python3
"""BaseModel module for AirBnB clone project."""

import uuid
from datetime import datetime
from models import storage  #Import storage instance


class BaseModel:
    """
    Base class for all AirBnB clone models with attributes and methods.
    """

    def __init__(self, *args, **kwargs):
        """
        Initialize a new BaseModel instance.

        If kwargs is provided, it recreates an instance from a dictionary.
        Otherwise, it creates a new instance with a unique ID and timestamps,
        and stores it in the storage engine.
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                if key in ("created_at", "updated_at"):
                    value = datetime.fromisoformat(value)
                setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            storage.new(self)  #Register new object in storage

    def __str__(self):
        """
        Return string representation of the BaseModel instance.
        Format: [<class name>] (<self.id>) <self.__dict__>
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        Update the 'updated_at' attribute with the current time
        and save the instance to the storage engine.
        """
        self.updated_at = datetime.now()
        from models import storage
        storage.save()  #Persist storage to file

    def to_dict(self):
        """
        Return a dictionary representation of the instance.
        """
        dict_rep = self.__dict__.copy()
        dict_rep["__class__"] = self.__class__.__name__
        dict_rep["created_at"] = self.created_at.isoformat()
        dict_rep["updated_at"] = self.updated_at.isoformat()
        return dict_rep
