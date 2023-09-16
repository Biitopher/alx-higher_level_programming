#!/usr/bin/python3
"""Script that prints the first State object from the database."""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys


def print_first_state(username, password, database_name):
    try:
        db_url = f"mysql://{username}:\
                {password}@localhost:3306/{database_name}"

        engine = create_engine(db_url)
        Session = sessionmaker(bind=engine)
        session = Session()

        first_state = session.query(State).order_by(State.id).first()

        if first_state:
            print(f"{first_state.id}: {first_state.name}")
        else:
            print("Nothing")

        session.close()

    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python script.py <username> <password> <database_name>")
    else:
        username, password, database_name = sys.argv[1],
        sys.argv[2], sys.argv[3]
        print_first_state(username, password, database_name)
