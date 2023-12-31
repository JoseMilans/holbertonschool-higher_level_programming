#!/usr/bin/python3
"""Module to define the City class
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from relationship_state import Base


class City(Base):
    """City class:
    - inherits from Base
    - links to the MySQL table cities
    - has id, name, and state_id attributes
    """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
