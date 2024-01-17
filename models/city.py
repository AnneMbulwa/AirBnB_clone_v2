#!/usr/bin/python3

from models.base_model import Base
from models.base_model import BaseModel
from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import relationship


class City(BaseModel, Base):
    """class city inherits from both the basemodel and base classes

    Attributes:
        name(sqlalchemy String): name of city
        state_id(sqlalchemy): city's state id
    """

    __tablename__ = "cities"
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), nullable=False, ForeignKey("states.id"))
    city = relationship("City", backref="cities")
