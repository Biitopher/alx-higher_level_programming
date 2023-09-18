#!/usr/bin/python3
"""Script to create State with City"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City


def create_state_city(username, password, db_name):
    """Create State "California" with City "San Francisco" in the database"""
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(username, password, db_name),
                           pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    california = State(name="California")

    san_francisco = City(name="San Francisco")

    san_francisco.state = california

    session.add(san_francisco)

    session.commit()

    session.close()


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <db_name>".format(sys.argv[0]))
        sys.exit(1)

    username, password, db_name = sys.argv[1], sys.argv[2], sys.argv[3]
    create_state_city(username, password, db_name)
