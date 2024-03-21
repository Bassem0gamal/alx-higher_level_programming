#!/usr/bin/python3

"""
This script deletes all State objects
with a name containing the letter `a`
from the database
"""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """
    Deletes State objects on the database
    """

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3]))
    Session = sessionmaker(bind = engine)
    session = Session()

    for ins in session.query(State).filter(State.name.contains('a')):
        session.delete(ins)

    session.commit()
    session.close()
