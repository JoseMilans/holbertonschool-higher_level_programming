#!/usr/bin/python3
"""Module to print the first State object from the database hbtn_0e_6_usa
"""
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv


def print_first_state(mysql_usr, mysql_pw, db_name):
    """Prints the first State object from the database
    """
    conn = f'mysql+mysqldb://{mysql_usr}:{mysql_pw}@localhost:3306/'
    engine = create_engine(conn + db_name)
    Session = sessionmaker(bind=engine)
    session = Session()

    first_state = session.query(State).order_by(State.id).first()

    if first_state:
        print(f'{first_state.id}: {first_state.name}')
    else:
        print('Nothing')

    session.close()


if __name__ == '__main__':
    if len(argv) == 4:
        print_first_state(argv[1], argv[2], argv[3])
