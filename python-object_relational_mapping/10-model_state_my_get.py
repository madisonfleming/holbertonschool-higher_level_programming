#!/usr/bin/python3
"""List all State objects with the name
passed as argument from the database using SQLalchemy
"""


import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker

from sqlalchemy import (create_engine)

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    state_name = sys.argv[4]
    Session = sessionmaker(bind=engine)
    session = Session()

    for a in sys.argv:
        if a.count(";"):
            exit()
    instance = session.query(State).where(State.name == state_name)
    if instance.count() == 0:
        print("Not found")
    else:
        for state in instance:
            print("{}".format(state.id))
