#!/usr/bin/python3
""" This module contains the class definition for the DBStorage engine """
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from os import getenv
from models.base_model import Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

classes = {"Amenity": Amenity, "City": City, "Place": Place,
           "Review": Review, "State": State, "User": User}


class DBStorage:
    """ Database storage engine for the HBNB project """
    __engine = None
    __session = None

    def __init__(self):
        """ Instantiation of DBStorage engine """
        user = getenv('HBNB_MYSQL_USER')
        pwd = getenv('HBNB_MYSQL_PWD')
        host = getenv('HBNB_MYSQL_HOST')
        db = getenv('HBNB_MYSQL_DB')
        self.__engine = create_engine(
            f'mysql+mysqldb://{user}:{pwd}@{host}/{db}', pool_pre_ping=True)

        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Queries current database session for all objects of a given class"""
        obj_dict = {}
        if cls:
            objs = self.__session.query(cls).all()
            for obj in objs:
                key = f'{obj.__class__.__name__}.{obj.id}'
                obj_dict[key] = obj
        else:
            for class_name in classes:
                objs = self.__session.query(classes[class_name]).all()
                for obj in objs:
                    key = f'{obj.__class__.__name__}.{obj.id}'
                    obj_dict[key] = obj
        return obj_dict

    def new(self, obj):
        """ Adds a new object to the current database session """
        self.__session.add(obj)

    def save(self):
        """ Commits all changes to the current database session """
        self.__session.commit()

    def delete(self, obj=None):
        """ Deletes an object from the current database session if not None """
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """ Reloads the database session from the engine """
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        self.__session = scoped_session(session_factory)()

    def close(self):
        """ Closes the current database session """
        self.__session.close()
