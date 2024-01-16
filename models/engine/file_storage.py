#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review

classes = {
        'BaseModel': BaseModel, 'User': User, 'Place': Place,
        'State': State, 'City': City, 'Amenity': Amenity,
        'Review': Review
        }

class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=name):
        """Returns a dictionary of models currently in storage"""
        if cls is not None:
            if type(cls) == str:
                cls = eval(cls)
            cls_dicx = {}
            for q, m in self.__objects.items():
                if type(m) == cls:
                    cls_dicx[q] = m
            return cls_dicx
        return self.__object


    def new(self, obj):
        """Adds new object to storage dictionary"""
        self.__objects["{}.{}".format(type(obj).__name__, obj.id)] = obj


    def save(self):
        """Saves storage dictionary to file"""
        xdict = {a: self.__objects[a].to_dict() for a in self.__objects.keys()}

        with open(self.__file_path, 'w', encoding="utf-8") as myfile:
            json.dump(xdict, myfile)

    def reload(self):
        """Loads storage dictionary from file"""
        try:
            with open(self.__file_path, 'r', encoding="utf-8") as myfile:
                for a in json.load(myfile).values():
                    name = a["__class__"]
                    del a["__class__"]
                    self.new(eval(name(**a)))
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """ to delete obj from __objects if it’s inside
        if obj is equal to None, the method should not do anything"""
        try:
            del self.__objects["{}.{}".format(type(obj).__name__, obj.id)]
        except(AttributeError, KeyError):
            pass
