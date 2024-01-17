#!/usr/bin/python3

from models.base_model import Base
from models.base_model import BaseModel
from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import relationship


class Review(BaseModel, Base):
    """
    Attributes:
        __tablename__ (str): MySQL tablename to store Reviews.
        text (sqlalchemy String): The review description.
        place_id (sqlalchemy String): review's place id.
        user_id (sqlalchemy String): review's user id.
    """
    __tablename__ = "reviews"
    text = Column(String(1024), nullable=False)
    place_id = Column(String(60), nullable=False, ForeignKey("places.id"))
    user_id = Column(String(60), nullable=False, ForeignKey("users.id"))
