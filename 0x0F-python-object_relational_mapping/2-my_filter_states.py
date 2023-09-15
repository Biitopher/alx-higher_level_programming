#!/usr/bin/python3
"""Script displaying all values in the states"""


import MySQLdb
import sys


def search_states(username, password, database, state_name):
    try:
        db = MySQLdb.connect(host='localhost', port=3306, user=username, passwd=password, db=database)

        cursor = db.cursor()

        query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"

        cursor.execute(query, (state_name,))

        results = cursor.fetchall()

        for row in results:
            print(row)

        cursor.close()
        db.close()

    except MySQLdb.Error as e:
        print("MySQL Error:", e)
        sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python script.py <username> <password> <database> <state_name>")
        sys.exit(1)

    username, password, database, state_name = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]
    search_states(username, password, database, state_name)
