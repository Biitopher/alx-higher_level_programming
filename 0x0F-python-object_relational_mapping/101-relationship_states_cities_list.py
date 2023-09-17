#!/usr/bin/python3
"""script listing State objects, and corresponding City objects in database"""


import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City

def list_states_and_cities(username, password, database):
    engine = create_engine(f'mysql://{username}:\
            {password}@localhost:3306/{database}')

    Session = sessionmaker(bind=engine)
    session = Session()

    states_and_cities = session.query(State, City).join(City).order_by(State.id, City.id).all()

    session.close()

    for state, city in states_and_cities:
        print(f"{state.name}: ({city.id}) {city.name}")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python script.py <username> <password> <database>")
    else:
        username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]
        list_states_and_cities(username, password, database)
