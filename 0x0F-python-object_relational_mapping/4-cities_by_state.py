#!/usr/bin/python3
"""script that lists all cities from the database"""


import MySQLdb
import sys


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python script.py <username> <password> <database_name>")
    else:
        try:
            db = MySQLdb.connect(user=sys.argv[1],
                                 passwd=sys.argv[2],
                                 db=sys.argv[3])
            c = db.cursor()

            c.execute("SELECT * FROM `cities` ORDER BY `id`")
            cities = c.fetchall()

            c.execute("SELECT `c`.`id`, `c`.`name`, `s`.`name` \
                         FROM `cities` as `c` \
                        INNER JOIN `states` as `s` \
                           ON `c`.`state_id` = `s`.`id` \
                        ORDER BY `c`.`id`")
            city_details = c.fetchall()

            for city_detail in city_details:
                print(city_detail)

        except MySQLdb.Error as e:
            print("MySQL Error:", e)
        finally:
            c.close()
            db.close()
