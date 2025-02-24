#!/usr/bin/python3

"""This module instantiates an object of class FileStorage
or DBStorage depending on the enviroment HBNB_TYPE_STORAGE
"""
from models.engine.file_storage import FileStorage
from models.engine.db_storage import DBStorage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import os

STORAGE_TYPE = os.getenv('HBNB_TYPE_STORAGE')

if STORAGE_TYPE == 'db':
    storage = DBStorage()
else:
    storage = FileStorage()

storage.reload()
