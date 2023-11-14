#!/usr/bin/python3
"""
Module to connect to a MySQL database and list all states
from the database hbtn_0e_0_usa
"""

import MySQLdb
from sys import argv


def list_states(mysql_usr, mysql_pw, db_name):
    """
    Connects to the MySQL database and prints all states in
    ascending order by id
    """
    db = MySQLdb.connect(host='host.docker.internal', user=mysql_usr,
                         passwd=mysql_pw, db=db_name)
    try:
        with db.cursor() as cursor:
            cursor.execute('SELECT * FROM states ORDER BY id ASC')
            for state in cursor:
                print(state)
    finally:
        db.close()


if __name__ == '__main__':
    if len(argv) == 4:
        list_states(argv[1], argv[2], argv[3])
