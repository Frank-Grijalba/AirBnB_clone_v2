#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.place import place_amenity
import models


class Amenity(BaseModel, Base):
    """
    Amenity class
    """
    __tablename__ = 'amenities'
    name = Column(String(128),
                  nullable=False)

    if models.STORAGE_TYPE == 'db':
        place_amenities = relationship("Place",
                                       secondary=place_amenity)
