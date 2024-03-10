#!/usr/bin/python3
"""Explains the FileStorage class"""
import json
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.state import State
from models.place import Place
from models.user import User
from models.review import Review


class FileStorage:
    """Abstract storage engine to be described

    Attributes:
        __file_path (str): the name of the file to save objects
        __objects (dict): a dictionary of initiated objects
    """
    __file_path = "file.json"
    __objects = {}

    def new(self, obj):
        """Set __objects obj with key <obj_class_name>.id"""
        ocname = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(ocname, obj.id)] = obj

    def save(self):
        """number __objects to the JSON file __file_path."""
        odict = FileStorage.__objects
        objdict = {obj: odict[obj].to_dict() for obj in odict.keys()}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(objdict, f)

    def all(self):
        """Return the dictionary __objects."""
        return FileStorage.__objects

    def reload(self):
        """Deserialize the JSON file __file_path to __objects, if available"""
        try:
            with open(FileStorage.__file_path) as f:
                objdict = json.load(f)
                for o in objdict.values():
                    cls_name = o["__class__"]
                    del o["__class__"]
                    self.new(eval(cls_name)(**o))
        except FileNotFoundError:
            return
