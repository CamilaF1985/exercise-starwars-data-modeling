import os
from sqlalchemy import Column, ForeignKey, Integer, String, create_engine
from sqlalchemy.orm import relationship, declarative_base
from eralchemy2 import render_er

Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'usuario'
    id = Column(Integer, primary_key=True)
    email = Column(String(250), unique=True, nullable=False)
    password = Column(String(250), nullable=False)
    fecha_subscripcion = Column(String(50), nullable=False)
    nombre = Column(String(250), nullable=False)
    apellido = Column(String(250), nullable=False)

class Planeta(Base):
    __tablename__ = 'planeta'
    id = Column(Integer, primary_key=True)
    diameter = Column(String(10), nullable=False)
    rotation_period = Column(String(10), nullable=False)
    orbital_period = Column(String(10), nullable=False)
    gravity = Column(String(20), nullable=False)
    population = Column(String(20), nullable=False)
    climate = Column(String(255), nullable=False)
    terrain = Column(String(255), nullable=False)
    surface_water = Column(String(10), nullable=False)
    name = Column(String(255), unique=True, nullable=False)

class Personaje(Base):
    __tablename__ = 'personaje'
    id = Column(Integer, primary_key=True)
    height = Column(String(10), nullable=False)
    mass = Column(String(10), nullable=False)
    hair_color = Column(String(255), nullable=False)
    skin_color = Column(String(255), nullable=False)
    eye_color = Column(String(255), nullable=False)
    birth_year = Column(String(10), nullable=False)
    gender = Column(String(20), nullable=False)
    name = Column(String(255), unique=True, nullable=False)
    homeworld_id = Column(Integer, ForeignKey('planeta.id'), nullable=False)
    homeworld = relationship('Planeta', back_populates='personajes')

class Favorito(Base):
    __tablename__ = 'favorito'
    id = Column(Integer, primary_key=True)
    usuario_id = Column(Integer, ForeignKey('usuario.id'), nullable=False)
    usuario = relationship('Usuario', back_populates='favoritos')
    planeta_id = Column(Integer, ForeignKey('planeta.id'), nullable=True)
    planeta = relationship('Planeta', back_populates='favoritos')
    personaje_id = Column(Integer, ForeignKey('personaje.id'), nullable=True)
    personaje = relationship('Personaje', back_populates='favoritos')

# Agregamos back_populates para establecer la relación bidireccional
Planeta.personajes = relationship('Personaje', order_by=Personaje.id, back_populates='homeworld')
Usuario.favoritos = relationship('Favorito', order_by=Favorito.id, back_populates='usuario')
Planeta.favoritos = relationship('Favorito', order_by=Favorito.id, back_populates='planeta')
Personaje.favoritos = relationship('Favorito', order_by=Favorito.id, back_populates='personaje')

# Draw from SQLAlchemy base
render_er(Base, 'diagram.png')

