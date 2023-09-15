#!/usr/bin/python3
"""Script displaying all values in the states"""


import sys
import MySQLdb


def main():
    if len(sys.argv) != 5:
        print("Usage: python \
                script.py <username> <password> <database> <state_name>")
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    try:
        connection = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=database
        )
        cursor = connection.cursor()

        query = "SELECT * FROM states WHERE name=%s ORDER BY id ASC"
        cursor.execute(query, (state_name,))
        results = cursor.fetchall()

        if not results:
            print("No states found with the name '{}'".format(state_name))
        else:
            for row in results:
                print(row)

    except MySQLdb.Error as e:
        print("Error:", e)
    finally:
        if connection:
            connection.close()


if __name__ == "__main__":
    main()
