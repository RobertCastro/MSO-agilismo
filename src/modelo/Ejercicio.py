from sqlalchemy import Column, String, Float, Integer, Date, Time
from .declarative_base import Base, engine

class Ejercicio(Base):
    __tablename__ = 'ejercicio'
    
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    nombre = Column(String, index=True)
    descripcion = Column(String, index=True)
    enlace = Column(String, index=True)
    calorias = Column(Float, index=True)
    repeticiones = Column(Integer, index=True)
    fecha = Column(Date, index=True)
    tiempo = Column(Time, index=True)

Base.metadata.create_all(bind=engine)
