#!/usr/bin/python3
"""
Empty for now

"""
from datetime import datetime
import uuid
import models


class BaseModel:
    """

    """
    def __init__(self, *args, **kwargs):
        '''
        Docs
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
        documentation goes here
        '''
        class_name = type(self).__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)

    def save(self):
        """
        save documentation
        """
        self.updated_at = datetime.now()
        models.storage.save()
