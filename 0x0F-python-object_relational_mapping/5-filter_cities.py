#!/usr/bin/python3
"""script that takes in the name of a state as an argument and lists"""


import MySQLdb
import sys


def list_cities_by_state(username, password, database_name, state_name):
    try:
        db = MySQLdb.connect(host="localhost", user=username,
                             passwd=password, db=database_name, port=3306)
        cur = db.cursor()

        query = """SELECT cities.name
                   FROM cities
                   INNER JOIN states ON states.id=cities.state_id
                   WHERE states.name=%s
                   ORDER BY cities.id ASC"""

        cur.execute(query, (state_name,))
        rows = cur.fetchall()

        for row in rows:
            print(row[0])

    except MySQLdb.Error as e:
        print(f"MySQL Error: {e}")
    finally:
        if db:
            db.close()


if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python script_name.py \
                <username> <password> <database_name> <state_name>")
        sys.exit(1)

    (username, password, database_name, state_name) = (sys.argv[1],
                                                       sys.argv[2],
                                                       sys.argv[3],
                                                       sys.argv[4])
    list_cities_by_state(username, password, database_name, state_name)
