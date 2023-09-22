from sqlalchemy import Column, String, Float, Integer, Date, Time
from .declarative_base import Base, engine
from sqlalchemy.orm import relationship

class Ejercicio(Base):
    __tablename__ = 'ejercicio'
    
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    nombre = Column(String, index=True)
    descripcion = Column(String, index=True)
    enlace = Column(String, index=True)
    calorias = Column(Integer, index=True)
    
    Entrenamiento = relationship('Entrenamiento', back_populates='ejercicio')
    
Base.metadata.create_all(bind=engine)
