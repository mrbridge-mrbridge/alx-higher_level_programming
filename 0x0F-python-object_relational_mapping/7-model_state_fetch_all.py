#!/usr/bin/python3
"""
lists all State objects from the database hbtn_0e_6_usa
must use the module SQLAlchemy
"""
import sqlalchemy
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    obj = session.query(State).order_by(State.id)
    for state in obj:
        print('{}: {}'.format(state.id, state.name))
    session.close()
