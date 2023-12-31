#!/usr/bin/python3
"""
Module to connect to a MySQL database and safely list all states
from the database hbtn_0e_0_usa where the name matches the user input
"""

import MySQLdb
from sys import argv


def safe_filter_states(mysql_user, mysql_pw, db_name, state_name):
    """
    Displays all values in the states table where name matches the argument
    and prevents SQL injection
    """
    db = MySQLdb.connect(host='localhost', port=3306,
                         user=mysql_user, passwd=mysql_pw, db=db_name)
    try:
        with db.cursor() as cur:
            query = ("SELECT * FROM states WHERE BINARY name = %s "
                     "ORDER BY id ASC")
            cur.execute(query, (state_name,))
            for state in cur:
                print(state)
    finally:
        db.close()


if __name__ == '__main__':
    if len(argv) == 5:
        safe_filter_states(argv[1], argv[2], argv[3], argv[4])
