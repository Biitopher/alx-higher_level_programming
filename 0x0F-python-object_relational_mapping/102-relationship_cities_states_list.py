#!/usr/bin/python3
""" lists all City objects from the database"""


import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_city import Base, City


def list_cities(username, password, database):
    engine = create_engine(f'mysql://{username}:\
            {password}@localhost:3306/{database}')

    Session = sessionmaker(bind=engine)
    session = Session()

    cities = session.query(City).order_by(City.id).all()

    session.close()

    for city in cities:
        print(f"{city.id}: {city.name} -> {city.state.name}")


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python script.py <username> <password> <database>")
    else:
        username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]
        list_cities(username, password, database)
