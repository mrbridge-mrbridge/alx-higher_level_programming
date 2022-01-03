#!/usr/bin/python3
"""
lists all City objects from the database hbtn_0e_101_usa
You must use the module SQLAlchemy
You must only use one query to the database
Results must be sorted in ascending order by states.id and cities.id
must use the state relationship for all State objects
"""

import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_city import City
from relationship_state import State, Base
from sys import argv

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3], pool_pre_ping=True))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    obj = session.query(City).join(State)
    for city in obj:
        print('{}: {} -> {}'.format(city.id, city.name, city.state.name))
