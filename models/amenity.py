#!/usr/bin/python3

from models.base_model import Base
from models.base_model import BaseModel
from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy.orm import relationship


class Amenity(BaseModel, Base):
    """Attributes:
        __tablename__ (str): MySQL tablename to store Amenities.
        name (sqlalchemy String): amenity name.
        place_amenities (sqlalchemy relationship): Place-Amenity relationship
    """

    __tablename__ = "amenities"
    name = Column(String(128), nullable=False)
    place_amenities = relationship("Place", secondary="place_amenity",
                                   viewonly=False)
