#!/usr/bin/python3
"""python file that contains the class definition of State and an instance"""


from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

Base = declarative_base()

class State(Base):
    """Defines state"""
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)


if __name__ == "__main__":
    db_url = "mysql://<username>:<password>@localhost:3306/<database_name>"

    engine = create_engine(db_url)

    from your_module_name import State
    Base.metadata.create_all(engine)
