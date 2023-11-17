#!/usr/bin/python3
"""Module to print the State object with the given name
from the database hbtn_0e_6_usa
"""
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv


def get_state(mysql_usr, mysql_pw, db_name, state_name):
    """Prints the State object with the specified name
    """
    conn = f'mysql+mysqldb://{mysql_usr}:{mysql_pw}@localhost:3306/{db_name}'
    engine = create_engine(conn)
    Session = sessionmaker(bind=engine)
    session = Session()

    state = session.query(State).filter(State.name == state_name).first()

    if state:
        print(state.id)
    else:
        print('Not found')

    session.close()


if __name__ == '__main__':
    if len(argv) == 5:
        get_state(argv[1], argv[2], argv[3], argv[4])
