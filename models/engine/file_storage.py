#!/usr/bin/python3
import json
import os


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def __init__(self):
        pass

    def all(self):
        return self.__objects

    def new(self, obj):
        self.__objects[obj.__class__.__name__ + "." + obj.id] = obj

    def save(self):
        with open(self.__file_path, 'w') as file:
            obj_dict = {key: obj.to_dict()
                        for key, obj in self.__objects.items()}
            json.dump(obj_dict, file)
    
    def reload(self):
        """Deserializes the JSON file to __objects."""
        if os.path.exists(self.__file_path):
            from models.base_model import BaseModel
            from models.user import User
            from models.state import State
            from models.city import City
            from models.amenity import Amenity
            from models.review import Review
            from models.place import Place

            with open(self.__file_path, 'r') as file:
                obj_dict = json.load(file)
                for key, value in obj_dict.items():
                    class_name, obj_id = key.split('.')
                    obj_class = eval(class_name)
                    self.__objects[key] = obj_class(**value)
