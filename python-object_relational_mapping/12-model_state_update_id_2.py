#!/usr/bin/python3
"""Change the name of a State Object
from the database using SQLalchemy
"""


import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker

from sqlalchemy import (create_engine)

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    instance = session.query(State).where(State.id == 2).limit(1).one()
    instance.name = "New Mexico"
    session.commit()
