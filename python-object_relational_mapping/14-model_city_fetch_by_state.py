#!/usr/bin/python3
"""Module to list all City objects from the database hbtn_0e_14_usa
along with their corresponding State names
"""
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv


def list_cities_by_state(mysql_usr, mysql_pw, db_name):
    """Lists all cities from the database along with their State names,
    sorted by city IDs
    """
    conn = f'mysql+mysqldb://{mysql_usr}:{mysql_pw}@localhost:3306/{db_name}'
    engine = create_engine(conn)
    Session = sessionmaker(bind=engine)
    session = Session()

    cities = session.query(City, State).join(State).order_by(City.id).all()
    for city, state in cities:
        print(f'{state.name}: ({city.id}) {city.name}')

    session.close()


if __name__ == '__main__':
    if len(argv) == 4:
        list_cities_by_state(argv[1], argv[2], argv[3])
