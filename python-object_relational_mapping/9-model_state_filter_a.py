#!/usr/bin/python3
"""Module to list all State objects containing 'a'
from the database hbtn_0e_6_usa
"""
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv


def list_states_containing_a(mysql_usr, mysql_pw, db_name):
    """List all states containing the letter 'a'
    """
    conn = f'mysql+mysqldb://{mysql_usr}:{mysql_pw}@localhost:3306/'
    engine = create_engine(conn + db_name)
    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State)\
                    .filter(State.name.like('%a%'))\
                    .order_by(State.id)
    for state in states:
        print(f'{state.id}: {state.name}')

    session.close()


if __name__ == '__main__':
    if len(argv) == 4:
        list_states_containing_a(argv[1], argv[2], argv[3])
