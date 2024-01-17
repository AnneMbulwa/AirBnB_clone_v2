#!/usr/bin/python3

import models
from os import getenv
from models.base_model import Base
from models.base_model import BaseModel
from models.amenity import Amenity
from models.review import Review
from sqlalchemy import Column
from sqlalchemy import Float
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Table
from sqlalchemy.orm import relationship

relation_table = Table("place_amenity", Base.metadata,
                       Column("place_id", String(60), ForeignKey("places.id"),
                              primary_key=True, nullable=False),
                       Column("amenity_id", String(60),
                              ForeignKey("amenities.id"), primary_key=True,
                              nullable=False)
                       )


class Place(BaseModel, Base):
    """
    Attributes:
    """

    __tablename__ = "places"
    city_id = Column(String(60), nullable=False, ForeignKey("cities.id"))
    user_id = Column(String(60), nullable=False, ForeignKey("users.id"))
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=False)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = (Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)

    reviews = relationship("Review", backref="place", cascade="delete")
    amenities = relationship("Amenity", secondary="place_amenity",
                             viewonly=False)

    amenity_ids = []

    if getenv("HBNB_TYPE_STORAGE", None) != "db":
        @property
        def reviews(self):
            """list of all linked Reviews."""
            mod = models.storage.all(Review)
            x_review = []
            for review in (mod.values()):
                if review.place_id == self.id:
                    x_review.append(review)
            return x_review

        @property
        def amenities(self):
            """list set of linked amenities"""
            mod = models.storage.all(Amenities)
            x_amenity = []
            for amenity in list(mod.values()):
                if amenity.id in self.amenity_ids:
                    x_amenity.append(amenity)
            return x_amenity

        @amenity.setter

        def amenities(self, value):
            if type(value) == Amenity:
                self.amenity_ids.append(value.id)
