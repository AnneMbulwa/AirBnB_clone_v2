#!/usr/bin/python3

from datetime import datatime
import models
from uuid import uuid4
from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import DateTime

Base = declarative_base()


class BaseModel:
    """basemodel class body

    Attributes:
        id (sqlalchemy string): class basemodel id
        create_at(sqlalchemy datetime): time created
        update_at(sqlalchemy datetime): last update time
    """

    id = Column(String(60), nullable=False, primary_key=True)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow())

    def __init__(self, *args, **kwargs):

        self.id = str(uuid4())
        self.created_at = self.updated_at = datetime.utcnow()

        if kwargs:
            for key, val in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    val = datetime.strptime(val, "%Y-%m-%dT%H:%M:%S.%f")
                if key != "__class__":
                    setattr(self, key, val)

    def save(self):
        """update update_at with the current time"""
        self.update_at = datetime.utcnow()
        models.storage.new(self)
        models.storage.save(self)

    def to_dict(self):
        """remove _sa_instance_state"""
        xdict = __dict__.copy()
        xdict["__class__"] = str(type(self).__name__)
        xdict["__created_at__"] = self.created_at.isoformat()
        xdict["__updated_at__"] = self.updated_at.isoformat()
        xdict.pop("_sa_instance_state", None)

        return xdict

    def delete(self):
        """deletes the current instance from the storage (models.storage)
        by calling the method delete"""
        models.storage.delete(self)

    def __str__(self):
        """string representation of created_at and updated_at"""
        return "[{}] ({}) {}".format(
                self.__class__.__name__, self.id, self.__dict__)
