#!/usr/bin/python3
"""
lists all State objects that contain the letter a from the database
hbtn_0e_6_usa
You must use the module SQLAlchemy
"""


import sqlalchemy
from model_city import Base, City
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sys import argv
from model_state import Base, State

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    for city, state in session.query(City, State)\
            .filter(City.state_id==State.id).order_by(City.id).all():
            print('{}: ({}) {}'.format(
                  state.name, city.id, city.name))

