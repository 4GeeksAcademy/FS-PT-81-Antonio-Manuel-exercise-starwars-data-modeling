import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Numeric
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key = True)
    name = Column(String, nullable = False)
    last_name = Column(String, nullable = False)
    email = Column(String, unique = True, nullable = False)
    password = Column(String, nullable = False)
    subscription_date = Column(String)
    fav = relationship('Favourite')

class Favourite(Base):
    __tablename__='favourite'
    favourite_id = Column(Integer, primary_key = True)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship('Users')
    character_id = Column(Integer, ForeignKey('characters.id'))
    characters = relationship('characters')
    planets_id = Column(Integer, ForeignKey('planets.id'))
    planets = relationship('planets')
    vehicles_id = Column(Integer, ForeignKey('vehicles.id'))
    vehicles = relationship('vehicles')


class Characters(Base):
    __tablename__ = 'characters'
    characters_id = Column(Integer, primary_key = True)
    url = Column(String, nullable = False)
    name = Column(String, nullable = False)
    birth_year = Column(String, nullable = True)
    gender = Column(String, nullable = True)
    eye_color = Column(String, nullable = True)
    hair_color = Column(String, nullable = True)
    skin_color = Column(String, nullable = True)
    height = Column(Numeric, nullable = True)
    mass = Column(Numeric, nullable = True)

class Planets(Base):
    __tablename__= 'planets'
    planets_id = Column(Integer, primary_key = True)
    url = Column(String, nullable = False)
    name = Column(String, nullable = False)
    description = Column(String, nullable = False)
    climate = Column(String, nullable = False)
    diameter = Column(Numeric, nullable = False)
    orbital_period = Column(Numeric, nullable = False)
    gravity = Column(Numeric, nullable = False)
    population = Column(Numeric, nullable = False)
    terrain = Column(String, nullable = False)
    surface_water = Column(Numeric, nullable = False)
    rotation_period = Column(Numeric, nullable = False)

class Vehicles(Base):
    __tablename__= 'vehicles'
    vehicles_id = Column(Integer, primary_key = True)
    url = Column(String, nullable = False)
    name = Column(String, nullable = False)
    model = Column(String, nullable = True)
    crew = Column(Numeric, nullable = True)
    passengers = Column(Numeric, nullable = True)
    length = Column(Numeric, nullable = True)
    cargo_capacity = Column(Numeric, nullable = True)







    def to_dict(self):
        return {}


try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
# Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
