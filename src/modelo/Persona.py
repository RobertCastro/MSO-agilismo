from sqlalchemy import Column, String, Date, Float, Integer, Boolean
from .declarative_base import Base, engine

<<<<<<< HEAD
class Persona(Base):
    __tablename__ = 'persona'
    
=======
 

class Persona(Base):
    __tablename__ = 'persona'

>>>>>>> 20e5b088ee77509a7669401e588857756425a46f
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
    fecha_inicio = Column(Date, index=True)
    fecha_retiro = Column(Date, index=True)
    razon_retiro = Column(String, index=True)
    estado = Column(Boolean, index=True)

<<<<<<< HEAD
# Crear todas las tablas
Base.metadata.create_all(bind=engine)
=======
 

# Crear todas las tablas
Base.metadata.create_all(bind=engine)
>>>>>>> 20e5b088ee77509a7669401e588857756425a46f
