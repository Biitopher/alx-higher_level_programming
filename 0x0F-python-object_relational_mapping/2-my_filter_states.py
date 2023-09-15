#!/usr/bin/python3
"""Script displaying all values in the states"""


import sys
import MySQLdb


if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python \
                script.py <username> <password> <database_name> <state_name>")
        sys.exit(1)

    username, password, database_name, state_name = (sys.argv[1],
    sys.argv[2], sys.argv[3], sys.argv[4])
    search_states(username, password, database_name, state_name)
