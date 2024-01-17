#!/usr/bin/python3

import models
from os import getenv
from models.base_model import Base
from models.base_model import BaseModel
from models.city import City
from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """class state body that inherits from basemodel and base

    Attributes:
        name(sqlalchemy string): name of state
    """

    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    citie = relationship("City", backref="state", cuscade="delete")

    def __init__(self, *args, **kwargs):
        """initializes State"""
        super().__init__(*args, **kwargs)

    if getenv("HBNB_TYPE_STORAGE") != "db":
        @property

        def cities(self):
            new_city = []
            val = models.storage.all(City)
            for city in val.values():
                if city.state_id == self.id:
                    val.append(city)
            return val
