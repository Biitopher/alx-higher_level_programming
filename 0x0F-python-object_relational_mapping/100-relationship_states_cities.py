#!/usr/bin/python3
"""Creates state with city from database"""


import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python \
                script.py <mysql_username> <mysql_password> <database_name>")
        sys.exit(1)

    engine = create_engine(f'mysql+mysqldb://{mysql_username}:\
            {mysql_password}@localhost:3306/{database_name}')

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    california = State(name='California')
    san_francisco = City(name='San Francisco', state=california)
    session.add(california)

    session.commit()
