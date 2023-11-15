#!/usr/bin/python3
"""
Module to connect to the MySQL database and list all cities of
a specified state from the database hbtn_0e_4_usa
"""

import MySQLdb
from sys import argv


def filter_cities():
    """
    List all cities of a given state in the database
    """
    db = MySQLdb.connect(host='localhost', port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])
    state_name = argv[4]

    with db.cursor() as cur:
        cur.execute("SELECT cities.name "
                    "FROM cities "
                    "JOIN states ON cities.state_id = states.id "
                    "WHERE BINARY states.name = %s "
                    "ORDER BY cities.id ASC", (state_name,))
        cities = [city[0] for city in cur]
        print(', '.join(cities))

    db.close()


if __name__ == '__main__':
    if len(argv) == 5:
        filter_cities()
