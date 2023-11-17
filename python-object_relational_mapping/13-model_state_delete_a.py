#!/usr/bin/python3
"""Module to delete all State objects with a name containing the letter 'a'
from the database hbtn_0e_6_usa
"""
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv


def delete_states_with_a(mysql_usr, mysql_pw, db_name):
    """Deletes all states with a name containing the letter 'a'
    """
    conn = f'mysql+mysqldb://{mysql_usr}:{mysql_pw}@localhost:3306/{db_name}'
    engine = create_engine(conn)
    Session = sessionmaker(bind=engine)
    session = Session()

    states_to_delete = session.query(State)\
                              .filter(State.name.like('%a%'))\
                              .all()
    for state in states_to_delete:
        session.delete(state)
    session.commit()
    session.close()


if __name__ == '__main__':
    if len(argv) == 4:
        delete_states_with_a(argv[1], argv[2], argv[3])
