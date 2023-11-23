#!/usr/bin/python3
"""Module to create the State 'California' with the City 'San Francisco'
in the database hbtn_0e_100_usa
"""
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv


def create_california_with_san_francisco(mysql_usr, mysql_pw, db_name):
    """Creates the State 'California' with the City 'San Francisco'
    """
    conn = f'mysql+mysqldb://{mysql_usr}:{mysql_pw}@localhost:3306/{db_name}'
    engine = create_engine(conn)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    california = State(name="California")
    san_francisco = City(name="San Francisco")
    california.cities.append(san_francisco)

    session.add(california)
    session.commit()

    print(san_francisco.id)

    session.close()


if __name__ == '__main__':
    if len(argv) == 4:
        create_california_with_san_francisco(argv[1], argv[2], argv[3])
#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
from sqlalchemy import Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
import models
import uuid
from datetime import datetime

Base = declarative_base()


class BaseModel:
    """A base class for all hbnb models"""
    # sqlalchemy model attrs
    id = Column(String(60), primary_key=True,
                default=lambda: str(uuid.uuid4()))
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow)
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow)

    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""
        if kwargs:
            kwargs['updated_at'] = datetime.strptime(kwargs['updated_at'],
                                                     '%Y-%m-%dT%H:%M:%S.%f')
            kwargs['created_at'] = datetime.strptime(kwargs['created_at'],
                                                     '%Y-%m-%dT%H:%M:%S.%f')
            kwargs.pop('__class__', None)  # remove class attr
            self.__dict__.update(kwargs)
        else:
            # initialise with default values if no kwargs
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def delete(self):
        """ Deletes the instance from storage """
        models.storage.delete(self)

    def to_dict(self):
        """Convert instance into dict format"""
        dictionary = self.__dict__.copy()
        dictionary['__class__'] = type(self).__name__
        dictionary['created_at'] = dictionary['created_at'].isoformat()
        dictionary['updated_at'] = dictionary['updated_at'].isoformat()
        dictionary.pop('_sa_instance_state', None)
        return dictionary
