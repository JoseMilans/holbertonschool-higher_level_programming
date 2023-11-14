#!/usr/bin/python3
"""
Module for a script that lists all states from the database hbtn_0e_0_usa
with a name starting with N
"""

import MySQLdb
from sys import argv


def list_states_n(mysql_usr, mysql_pw, db_name):
    """
    Lists all states with a name starting with N from the database
    """
    db = MySQLdb.connect(host='localhost', user=mysql_usr,
                         passwd=mysql_pw, db=db_name)
    try:
        with db.cursor() as cur:
            cur.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%' "
                        "ORDER BY id ASC")
            for state in cur:
                print(state)
    finally:
        db.close()


if __name__ == '__main__':
    if len(argv) == 4:
        list_states_n(argv[1], argv[2], argv[3])
