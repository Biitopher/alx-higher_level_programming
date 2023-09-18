#!/usr/bin/python3
"""Script to list State and City objects from the database using SQLAlchemy"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_city import City
from relationship_state import Base, State


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python \
                script.py <mysql_username> <mysql_password> <database_name>")
        sys.exit(1)

    mysql_username, mysql_password, database_name = (sys.argv[1],
                                                     sys.argv[2], sys.argv[3])

    engine = create_engine(f'mysql+mysqldb://{mysql_username}:\
            {mysql_password}@localhost:3306/{database_name}')

    Session = sessionmaker(bind=engine)
    session = Session()

    query = session.query(State).order_by(State.id).all()

    for state in query:
        print(f"{state.id}: {state.name}")
        for city in state.cities:
            print(f"    {city.id}: {city.name}")

    session.close()
