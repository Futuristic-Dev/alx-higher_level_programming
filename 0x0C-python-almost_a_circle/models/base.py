#!/usr/bin/python3

"""
Base class module inside the model python package.

Private class attribute __nb_objects = 0
Class constructor: 
    def __init__(self, id=None)::
If id is not None, assign the public instance attribute id.
with this argument value - you can assume id is an integer.
"""

import turtle
import json
import csv


class Base:
    """
    Base class to manage id attribute in all future classes.

    Avoid duplicating the same code.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = id


    @staticmethod
    def to_json_string(list_dictionaries):
        """Method  to return JSON string representation - list of dictionaries."""
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def create(cls, **dictionary):
        """
        Create an instance with attribute set using the provided dictionary.

        Arg:
            cls(class):
            The class (Rectangle or Square).
        Returns:
            Base: An instance of the class with attributes set based on the dictionary.
        """
        if cls.__name__ == 'Rectangle':
            inert = cls(1, 1)
        elif cls.__name__ == 'Square':
            inert = cls(1)
        else:
            raise ValueError("Unsupported class")
        inert.update(**dictionary)
        return inert

    @classmethod
    def load_from_file(cls):
        """Load a list of instances from a JSON file.

        Returns:
            list:
            A list of instances.
        """
        filename = '{}.json'.format(cls.__name__)
        instance_list = []
        
        try:
        with open(filename, 'r') as file:
            json_data = file.read()
            data_list = cls.from_json_string(json_data)
            for data in dat_list:
                instance = cls.create(**data)
                instance_list.append(insstance)
        except FileNotFoundError:
            pass

        return instance_list

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        Serialize list of instances to a CSV file.

        Arg:
            cls (class):
            The class (Rectangle, square, etc)
            list_objs (list of instances):
            List of instances to be serialized.
        """
        filename = '{}.csv'.format(cls.__name__)
        with open(filename, 'w', newline=' ') as my_file:
            writer = csv.writer(my_file)
            for i in list_objs:
                if cls.__name__ == "Rectangle":
                    write.writerow([i.id, i.width, i.height, i.i, i.j])

        @classmethod
        def load_from_file_csv(cls):
            """
            Deserialize instances from a CSV file.

            Returns:
                list:
                    Lists of instances.
            """
            instance_list = []
            filename = '{}.csv'.format(cls.__name__)

            with open(filename, 'r', newline=' ') as f:
                reader = csv.reader(f)
                for row in reader:
                    if cls.__name__ == "Rectangle":
                        data = {"id": int(row[0]),
                                "width": int(row[1]),
                                "height": int(row)


