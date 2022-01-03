#!/usr/bin/python3
"""
contains the class definition of a City and an instance
Base = declarative_base()
City class:
inherits from Base
links to the MySQL table cities
"""


import sqlalchemy
from sqlalchemy import Column, Integer, String, ForeignKey
from relationship_state import Base, State
from sqlalchemy.orm import relationship

class City(Base):
    """class that represents a City in MySQL db"""
    __tablename__ = 'cities'
    id = Column(Integer, unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'))
    state = relationship('State', back_populates='cities')
