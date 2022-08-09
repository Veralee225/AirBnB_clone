#!/usr/bin/python3
""" Module for file storage """

import os
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """ Serializes instances to a JSON file and
    deserializes JSON file to instances
    Args:
    __file_path - path to the JSON file
    __objects - dictionary - store all objects by
        <class name>.id
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ Returns: __objects """

        return FileStorage.__objects

    def new(self, obj):
        """ sets in __objects the obj with key
        <obj class name>.id """

        FileStorage.__objects["{}.{}".
                              format(type(obj).__name__, obj.id)] = obj

    def save(self):
        """ serializes __objects to the JSON file
        (path: __file_path) """

        try:
            my_dict = {}
            for key, value in FileStorage.__objects.items():
                my_dict[key] = value.to_dict()

            with open(FileStorage.__file_path, 'w') as f:
                json.dump(my_dict, f)
        except TypeError:
            pass

    def reload(self):
        """ deserializes the JSON file to __objects """

        try:
            with open(FileStorage.__file_path, 'r') as f:
                for key, value in (json.load(f)).items():
                    value = eval(value["__class__"])(**value)
                    FileStorage.__objects[key] = value
        except Exception:
            pass
