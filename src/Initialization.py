from src.modelo.declarative_base import Session
from src.modelo.Persona import Persona
from src.modelo.Ejercicio import Ejercicio
from src.modelo.Entrenamiento import Entrenamiento
from faker import Faker
from datetime import date, time
import random
from datetime import date

def poblar_tabla_personas():
    session = Session()
    data_factory = Faker()

    if not session.query(Persona).first():

        for _ in range(10):
            persona = Persona(
                nombre=data_factory.first_name(),
                apellido=data_factory.last_name(),
                edad=data_factory.random_int(min=18, max=100),
                talla=data_factory.pyfloat(left_digits=1, right_digits=3, positive=True, min_value=1.50, max_value=2.00),
                peso=data_factory.pyfloat(left_digits=2, right_digits=1, positive=True, min_value=50.0, max_value=100.0),
                brazo=data_factory.pyfloat(left_digits=2, right_digits=1, positive=True, min_value=20.0, max_value=50.0),
                pecho=data_factory.pyfloat(left_digits=3, right_digits=1, positive=True, min_value=60.0, max_value=120.0),
                cintura=data_factory.pyfloat(left_digits=3, right_digits=1, positive=True, min_value=60.0, max_value=120.0),
                pierna=data_factory.pyfloat(left_digits=2, right_digits=1, positive=True, min_value=40.0, max_value=80.0)
            )
            session.add(persona)
        
        session.commit()
    session.close()

def poblar_tabla_ejercicio():
    session = Session()
    data_factory = Faker()

    if not session.query(Ejercicio).first():

        for _ in range(10):
            ejercicio = Ejercicio(
                nombre=data_factory.unique.first_name(),
                descripcion=data_factory.text(max_nb_chars=200),
                enlace=data_factory.url(),
                calorias=random.randint(50, 500),
            )
            session.add(ejercicio)
        
        session.commit()
    session.close()
    
def poblar_tabla_entrenamiento():
    session = Session()
    data_factory = Faker()

    personas_ids = [persona.id for persona in session.query(Persona).all()]
    ejercicios_ids = [ejercicio.id for ejercicio in session.query(Ejercicio).all()]

    if not session.query(Entrenamiento).first():
        
        for _ in range(10):
            if personas_ids and ejercicios_ids:
                entrenamiento = Entrenamiento(
                    fecha=random_date(),
                    repeticiones=random.randint(5, 100),
                    tiempo = random_time(),
                    persona_id=random.choice(personas_ids),
                    ejercicio_id=random.choice(ejercicios_ids)
                )
                session.add(entrenamiento)
        
        session.commit()
    session.close()

def random_time():
    hora = str(random.randint(0, 23)).zfill(2)
    minuto = str(random.randint(0, 59)).zfill(2)
    segundo = str(random.randint(0, 59)).zfill(2)
    
    tiempo = f"{hora}:{minuto}:{segundo}"
    return tiempo

def random_date(start_year=2000, end_year=2023):
    year = random.randint(start_year, end_year)
    month = random.randint(1, 12)
    day = random.randint(1, 28)
    return f"{year}-{month:02d}-{day:02d}"