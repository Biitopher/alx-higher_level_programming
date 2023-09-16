#!/usr/bin/python3
"""python file that contains the class definition of State and an instance"""


import sys
from model_state import Base, State

from sqlalchemy import (create_engine)

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           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pool_pre_ping=True)

    Base.metadata.create_all(engine)
