#!/usr/bin/python3
'''
Module Docs
'''
from json import dumps, loads
from os.path import isfile
from models.base_model import BaseModel


class FileStorage:
    '''
    The FileStorage class handles serialization and deserialization of instances to and from JSON files.

    Attributes:
        __file_path (str): The file path to the JSON file.
        __objects (dict): A dictionary containing instances in the format {class_name.id: instance}.

    Methods:
        all: Returns the dictionary of all objects.
        new: Adds a new object to the dictionary.
        save: Serializes objects to JSON and saves to file.
        reload: Deserializes JSON file and loads objects into dictionary.
    '''
    __file_path = "file.json"
    __objects = {}

    def all(self):
        '''
        Returns a dictionary of all objects.
        
        Returns:
            dict: A dictionary containing all objects.
        '''
        return FileStorage.__objects

    def new(self, obj):
        '''
        Adds a new object to the dictionary.

        Args:
            obj: The object to be added.
        '''
        key = f"{obj.__class__.__name__}.{obj.id}"

        FileStorage.__objects[key] = obj

    def save(self):
        '''
        Serializes objects to JSON and saves to file.
        '''
        final_dict = {
                key: value.to_dict() for key, value
                in FileStorage.__objects.items()}
        json_string = dumps(final_dict)
        filename = FileStorage.__file_path
        with open(filename, "w") as f:
            f.write(json_string)

    def reload(self):
        '''
        Deserializes JSON file and loads objects into dictionary.
        '''
        filename = FileStorage.__file_path
        if isfile(filename):
            with open(filename, "r") as f:
                json_string = f.read()
                final_dict = loads(json_string)
            for key, value in final_dict.items():
                class_name, obj_id = key.split(".")
                if class_name == "BaseModel":
                    self.new(BaseModel(**value))
