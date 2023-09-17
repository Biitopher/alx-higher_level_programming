#!/usr/bin/python3
"""Creates state with city from database"""


import sys
from models import Base, State, City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    if len(sys.argv) != 4:
        print("Usage: python 100-relationship_states_cities.py \
                <username> <password> <database_name>")
        sys.exit(1)

    engine = create_engine(f'mysql+mysqldb://{sys.argv[1]}:\
            {sys.argv[2]}@localhost:3306/{sys.argv[3]}', pool_pre_ping=True)

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    california = State(name='California')

    san_francisco = City(name='San Francisco', state=california)

    session.add(california)
    session.add(san_francisco)

    session.commit()
