#!/usr/bin/python3
"""
lists all State objects that contain the letter a from the database
hbtn_0e_6_usa
You must use the module SQLAlchemy
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

    obj = session.query(State).filter_by(name = argv[4]).first()
    if obj is None:
        print('Not found')
    else:
        print(str(obj.id))
    session.close()
