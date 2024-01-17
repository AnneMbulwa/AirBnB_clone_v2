#!/usr/bin/python3
"""DBstorage engine"""

from os import getenv
from models.base_model import Base
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from sqlalchemy import create_engine
from sqlalchemy.orm import relationship
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker

user = getenv("HBNB_MYSQL_USER")
passwd = getenv("HBNB_MYSQL_PWD")
host = getenv("HBNB_MYSQL_HOST")
db = getenv("HBNB_MYSQL_DB")

class DBStorage:

    __engine = None
    __session = None

    def __init__(self):
        """create the engine (self.__engine)"""
        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}"
                                      .format(user,
                                              passwd,
                                              host,
                                              db),
                                      pool_pre_ping=True)
        if getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)
    
    def all(self, cls=None):
        """query on the current database session (self.__session)"""
        if cls is None:
            ses = self.__session.query(State).all()
            ses.extend(self.__session.query(City).all())
            ses.extend(self.__session.query(User).all())
            ses.extend(self.__session.query(Place).all())
            ses.extend(self.__session.query(Review).all())
            ses.extend(self.__session.query(Amenity).all())
        else:
            if type(cls) == str:
                cls = eval(cls)
            ses = self.__session.query(cls)
        return {"{}.{}".format(type(a).__name__, a.id): a for a in ses}

    def new(self, obj):
        """add the object to the current database session (self.__session)"""
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """create all tables in the database"""
        Base.metadata.create_all(engine)
        sew = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sew)

        self.__session = Session()

    def close():
        """closing sqlalchemy session"""
        self.__session.close()
