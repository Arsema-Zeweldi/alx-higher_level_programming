#!/usr/bin/python3
"""It manages the id attribute in all future classes"""
import json


class Base:
    """The Base class"""
    __nb_objects = 0
    def __init__(self, id=None):
        """private instance attribute"""
        if id != None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        """returns the string representation of list_dictionaries"""
        if list_dictionaries == None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    def save_to_file(cls, list_objs):
        filename = cls.__name__ + ".json"
        text = []
        if list_objs is not None:
            for list1 in list_objs:
                text.append(list1.to_dictionary())
        with open(filename, mode='w', encoding="utf-8") as MyFile:
            return MyFile.write(Base.to_json_string(text))

    def from_json_string(json_string):
        if json_string == None:
            return "[]"
        else:
            return json.loads(json_string)

    def create(cls, **dictionary):
        if cls.__name__ == "Rectangle":
            tmp = cls(10, 10)
        elif cls.__name__ == "Square":
            tmp = cls(10, 10)
        tmp.update(**dictionary)
        return tmp

    def load_from_file(cls):
        filename = cls.__name__ + ".json"
        new = []
        with open(filename) as MyFile:
            file_str = MyFile.read().replace('\n', '')
            data = cls.from_json_string(file_str)
            for c in data:
                new.append(cls.create(**c))

        return new
