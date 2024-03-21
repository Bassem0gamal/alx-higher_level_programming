#!/usr/bin/python3
"""
This script changes the name of a State object
from the database
"""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """
    Updates a State object on the database
    """
 
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    new_ins = session.query(State).filter(State.id == '2').first()
    new_ins.name = 'New Mexico'
    session.commit()
    session.close()
