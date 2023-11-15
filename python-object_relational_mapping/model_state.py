#!/usr/bin/python3
"""Module to define the State class and an instance of declarative base
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """State class:
    - inherits from Base
    - links to the MySQL table states
    - has an id and a name attribute
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
