#!/usr/bin/python3
"""
Module to connect to the MySQL database and list all cities
from the database hbtn_0e_4_usa along with their corresponding state names
"""

import MySQLdb
from sys import argv


def list_cities(mysql_user, mysql_pw, db_name):
    """
    Displays all cities from the database along with their state names
    sorted by city IDs
    """
    db = MySQLdb.connect(host='host.docker.internal', port=3306,
                         user=mysql_user, passwd=mysql_pw, db=db_name)
    try:
        with db.cursor() as cur:
            query = ("SELECT cities.id, cities.name, states.name "
                     "FROM cities "
                     "JOIN states ON cities.state_id = states.id "
                     "ORDER BY cities.id ASC")
            cur.execute(query)
            for city in cur:
                print(city)
    finally:
        db.close()


if __name__ == '__main__':
    if len(argv) == 4:
        list_cities(argv[1], argv[2], argv[3])
