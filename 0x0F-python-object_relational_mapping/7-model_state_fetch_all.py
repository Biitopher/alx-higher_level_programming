#!/usr/bin/python3
"""script that lists all State objects from the database"""


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys


def list_states(username, password, database_name):
    try:
        db_url = f"mysql://{username}:\
                {password}@localhost:3306/{database_name}"

        engine = create_engine(db_url)

        Session = sessionmaker(bind=engine)
        session = Session()

        states = session.query(State).order_by(State.id).all()

        if states:
            for state in states:
                print(f"{state.id}: {state.name}")
        else:
            print("No states found in the database.")

        session.close()

    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python \
                script.py <username> <password> <database_name>")
    else:
        (username, password, database_name) = (sys.argv[1],
                                               sys.argv[2], sys.argv[3])
    list_states(username, password, database_name)
