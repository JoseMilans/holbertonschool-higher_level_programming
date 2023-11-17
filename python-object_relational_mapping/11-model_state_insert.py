#!/usr/bin/python3
"""Module to add a new State object "Louisiana" to the database hbtn_0e_6_usa
"""
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv


def add_new_state(mysql_usr, mysql_pw, db_name):
    """Adds a new State object "Louisiana" to the database
    """
    conn = f'mysql+mysqldb://{mysql_usr}:{mysql_pw}@localhost:3306/{db_name}'
    engine = create_engine(conn)
    Session = sessionmaker(bind=engine)
    session = Session()

    new_state = State(name="Louisiana")
    session.add(new_state)
    session.commit()

    print(new_state.id)

    session.close()


if __name__ == '__main__':
    if len(argv) == 4:
        add_new_state(argv[1], argv[2], argv[3])
