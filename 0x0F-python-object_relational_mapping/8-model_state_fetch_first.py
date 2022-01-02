#!/usr/bin/python3
"""
prints the first State object from the database hbtn_0e_6_usa
must use the module SQLAlchemy
If the table states is empty, print Nothing followed by a new line
"""

import sqlalchemy
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sys import argv

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    obj = session.query(State).filter(State.id == 1)
    for state in obj:
        print('{}: {}'.format(state.id, state.name))
    session.close()
