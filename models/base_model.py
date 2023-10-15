#!/usr/bin/python3
"""
Empty for now

"""
from datetime import datetime
import uuid
import models


class BaseModel:
    """
    Base class for all models.

    Attributes:
        id (str): Unique identifier for the instance.
        created_at (datetime): Date and time of instance creation.
        updated_at (datetime): Date and time of instance last update.

    Methods:
        __init__: Initializes a new instance of BaseModel.
        __str__: Returns a string representation of the instance.
        save: Updates the instance's `updated_at` attribute
        and saves the changes.
        to_dict: Returns a dictionary representation of the instance.
    """
    def __init__(self, *args, **kwargs):
        '''
        Initializes a new instance of BaseModel.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.
        '''
        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at':
                    value = datetime.fromisoformat(value)
                    self.created_at = value
                elif key == 'updated_at':
                    value = datetime.fromisoformat(value)
                    self.updated_at = value
                elif key == 'id':
                    self.id = str(value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)

    def __str__(self):
        '''
        Returns a string representation of the instance.

        Returns:
            str: A formatted string containing class name, id, and attributes.
        '''
        class_name = type(self).__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)

    def save(self):
        """
        Updates the instance's `updated_at` attribute and saves the changes.
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        '''
        Returns a dictionary representation of the instance.

        Returns:
            dict: A dictionary containing class attributes and their values.
        '''
        dictionary = self.__dict__.copy()
        dictionary["__class__"] = type(self).__name__
        dictionary["created_at"] = self.created_at.isoformat()
        dictionary["updated_at"] = self.updated_at.isoformat()

        return dictionary
