#!/usr/bin/python3
"""Script listing all states"""


import sys
import MySQLdb


def list_states(username, password, database_name):
    try:
        connection = MySQLdb.connect(
            host='localhost',
            user=username,
            passwd=password,
            db=database_name,
            port=3306
        )

        cursor = connection.cursor()

        cursor.execute("SELECT * FROM states ORDER BY states.id ASC")

        states = cursor.fetchall()

        for state in states:
            print(state)

        cursor.close()
        connection.close()

    except MySQLdb.Error as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python script.py <username> <password> <database_name>")
        sys.exit(1)

    username, password, database_name = sys.argv[1], sys.argv[2], sys.argv[3]
    list_states(username, password, database_name)
