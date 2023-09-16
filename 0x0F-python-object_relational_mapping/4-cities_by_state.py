#!/usr/bin/python3
"""script that lists all cities from the database"""


import MySQLdb
import sys

def list_cities(username, password, database):
    try:
        db = MySQLdb.connect(host='localhost', port=3306, user=username, passwd=password, db=database)

        cursor = db.cursor()

        query = "SELECT * FROM cities ORDER BY id ASC"
        query = ("SELECT `c`.`id`, `c`.`name`, `s`.`name` \
                 FROM `cities` as `c` \
                INNER JOIN `states` as `s` \
                   ON `c`.`state_id` = `s`.`id` \
                ORDER BY `c`.`id`")

        cursor.execute(query)

        results = cursor.fetchall()

        for row in results:
            print(row)

        cursor.close()
        db.close()

    except MySQLdb.Error as e:
        print("MySQL Error:", e)
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python script.py <username> <password> <database>")
        sys.exit(1)

    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]
    list_cities(username, password, database)
