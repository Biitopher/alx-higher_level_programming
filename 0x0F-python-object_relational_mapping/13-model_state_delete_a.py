#!/usr/bin/python3
"""Deletes state onjects with letter 'a' from database"""


import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python \
                script.py <mysql_username> <mysql_password> <database_name>")
        sys.exit(1)

    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    engine = create_engine(f'mysql+mysqldb://{mysql_username}:\
            {mysql_password}@localhost:3306/{database_name}')

    Session = sessionmaker(bind=engine)
    session = Session()

    states_to_delete = session.query(State)\
        .filter(State.name.like('%a%')).all()

    if states_to_delete:
        for state in states_to_delete:
            session.delete(state)

        session.commit()
        print(f"Deleted {len(states_to_delete)} \
                State(s) with names containing 'a'")
    else:
        print("No State objects with names \
                containing 'a' found in the database.")
