from sqlalchemy import Column, String, Date, Float, Integer, Boolean
from .declarative_base import Base, engine
from sqlalchemy.orm import relationship

class Persona(Base):
    __tablename__ = 'persona'
    
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    nombre = Column(String, index=True)
    apellido = Column(String, index=True)
    edad = Column(Integer, index=True)
    talla = Column(Float, index=True)
    peso = Column(Float, index=True)
    brazo = Column(Float, index=True)
    pecho = Column(Float, index=True)
    cintura = Column(Float, index=True)
    pierna = Column(Float, index=True)
    fecha_inicio = Column(String, index=True)
    fecha_retiro = Column(String, index=True, default="")
    razon_retiro = Column(String, index=True)
    estado = Column(Boolean, index=True)
    
    Entrenamiento = relationship('Entrenamiento', cascade='all, delete-orphan') 

Base.metadata.create_all(bind=engine)
