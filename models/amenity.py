#!/usr/bin/python3
"""
Amenity Module
"""
import os
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import backref
storage_type = os.environ.get('HBNB_TYPE_STORAGE')


class Amenity(BaseModel, Base):
    """Amenity class """
    if storage_type == "db":
        __tablename__ = 'amenities'
        name = Column(String(128), nullable=False)
        place_amenities = relationship('PlaceAmenity', backref='amenities',
                                       cascade='delete')
    else:
        name = ''
