#!/usr/bin/python3
"""Module to change the name of a State object with id = 2 to 'New Mexico'
in the database hbtn_0e_6_usa
"""
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv


def update_state(mysql_usr, mysql_pw, db_name):
    """Changes the name of the State object with id = 2 to 'New Mexico'
    """
    conn = f'mysql+mysqldb://{mysql_usr}:{mysql_pw}@localhost:3306/{db_name}'
    engine = create_engine(conn)
    Session = sessionmaker(bind=engine)
    session = Session()

    state_to_update = session.query(State).filter(State.id == 2).first()
    if state_to_update:
        state_to_update.name = 'New Mexico'
        session.commit()

    session.close()


if __name__ == '__main__':
    if len(argv) == 4:
        update_state(argv[1], argv[2], argv[3])
