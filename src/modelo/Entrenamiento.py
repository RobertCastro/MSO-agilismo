from sqlalchemy import Column, String, Integer, Date, ForeignKey, Time 
from .declarative_base import Base, engine
from sqlalchemy.orm import relationship

class Entrenamiento(Base): 
    __tablename__ = 'entrenamiento' 

    id = Column(Integer, primary_key=True)
    fecha = Column(String) 
    repeticiones = Column(Integer)
    tiempo = Column(String)
    persona_id = Column(Integer, ForeignKey('persona.id')) 
    ejercicio_id = Column(Integer, ForeignKey('ejercicio.id')) 

    persona = relationship('Persona')
    ejercicio = relationship('Ejercicio')

Base.metadata.create_all(bind=engine)
