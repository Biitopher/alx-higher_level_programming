#!/usr/bin/python3
"""script that takes in the name of a state as an argument and lists"""


import MySQLdb
import sys


def filter_cities(username, password, database_name, state_name):
    """ Function to filter cities by state """
    try:
        db = MySQLdb.connect(host='localhost',
                             port=3306,
                             user=username,
                             passwd=password,
                             db=database_name)
        c = db.cursor()
        query = ("SELECT cities.name FROM cities "
                 "INNER JOIN states ON cities.state_id = states.id "
                 "WHERE states.name = %s "
                 "ORDER BY cities.id ASC")
        c.execute(query, (state_name,))
        results = cursor.fetchall()
        print(results)
        city_names = ', '.join(city[0] for city in cities)
        print(city_names)
    except MySQLdb.Error as e:
        print("MySQL Error: ", e)
        sys.exit(1)
