#!/usr/bin/python3
"""
Module for project Base class.
The “base” class to manage id attribute across subclasses
and to avoid duplicating the same code.
"""
import json


class Base:
    """
    Representation of Base class.

    Attrs:
        id: An ID for instances.

    Class attrs:
        __nb_objects: Keeps count of the number of instances created.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initialises Base class obj with an ID.

        Args:
            id (int, optional): An ID for the instance.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
    
    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Converts a list of dictionaries to its JSON string representation.
        """
        if not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Save the JSON string representation of list_objs to a file.
        """
        filename = f"{cls.__name__}.json"
        list_dicts = []
        
        if list_objs:
            for obj in list_objs:
                list_dicts.append(obj.to_dictionary())

        with open(filename, "w") as file:
            file.write(cls.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """
        Convert a JSON string representation into a list.
        """
        if not json_string:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Create an instance with all attributes already set using a dictionary.
        """
        if cls != Base:
            dum_obj = cls(1, 1)
            dum_obj.update(**dictionary)
            return dum_obj

    @classmethod
    def load_from_file(cls):
        """
        Load a list of class instances stored in a JSON class file.
        """
        filename = f"{cls.__name__}.json"
        objs_list = []
        try:
            with open(filename, "r") as file:
                cls_objs = cls.from_json_string(file.read())
            for obj in cls_objs:
                objs_list.append(cls.create(**obj))
        except FileNotFoundError:
            pass
        return objs_list
