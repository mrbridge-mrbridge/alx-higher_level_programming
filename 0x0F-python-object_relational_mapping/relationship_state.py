#!/usr/bin/python3
"""
contains the class definition of a State and an instance
Base = declarative_base()
State class:
inherits from Base
links to the MySQL table states
has relationship with cities
"""


import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import relationship

Base = declarative_base()


class State(Base):
    """class that represents a State in MySQL db"""
    __tablename__ = 'states'
    id = Column(Integer, unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    cities = relationship('City', back_populates='state',
                          cascade='all, delete, delete-orphan')
