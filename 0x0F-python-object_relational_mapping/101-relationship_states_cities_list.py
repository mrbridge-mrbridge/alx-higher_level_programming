#!/usr/bin/python3
"""
lists all State objects, and corresponding City objects, contained in the
database hbtn_0e_101_usa
You must use the module SQLAlchemy
You must only use one query to the database
Results must be sorted in ascending order by states.id and cities.id
must use the cities relationship for all State objects
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

    obj = session.query(State).order_by(State.id)
    for state in obj:
        print('{}: {}'.format(state.id, state.name))
        for city in state.cities:
            print('    {}: {}'.format(city.id, city.name))
