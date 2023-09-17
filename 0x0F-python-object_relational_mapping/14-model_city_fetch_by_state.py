#!/usr/bin/python3
"""Script printing all cities in the database"""


import sys
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python 14-model_city_fetch_by_state.py \
                <mysql_username> <mysql_password> <database_name>")
        sys.exit(1)

    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    engine = create_engine(f'mysql+mysqldb://{mysql_username}:\
            {mysql_password}@localhost:3306/{database_name}')

    Session = sessionmaker(bind=engine)
    session = Session()

    cities = session.query(City).order_by(City.id).all()

    for city in cities:
        state = session.query(State).filter_by(id=city.state_id).first()
        if state is not None:
            print(f"{state.name}: ({city.id}) {city.name}")

    session.close()
