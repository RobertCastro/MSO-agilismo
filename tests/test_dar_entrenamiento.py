import unittest
from src.modelo.declarative_base import Session
from src.logica.EntrenamientoEnForma import EntrenamientoEnForma
from src.modelo.Entrenamiento import Entrenamiento
from src.modelo.Ejercicio import Ejercicio
from src.modelo.Persona import Persona
from sqlalchemy import Time, Date
from datetime import date, time
from faker import Faker
import random

class TestDarEntrenamientos(unittest.TestCase):
    
    def setUp(self):
        self.data_factory = Faker()
        Faker.seed(1000)
        self.session = Session()
        self.session.query(Entrenamiento).delete()  
        self.session.commit()

        self.persona={
                'id': 1,
                'nombre': self.data_factory.first_name(),
                'apellido': self.data_factory.last_name(),
            }

    def test_listar_entrenamiento_vacio(self):
 
        entrenamiento_en_forma = EntrenamientoEnForma()
        dar_entrenamiento = entrenamiento_en_forma.dar_entrenamientos(self.persona['id'])
        self.assertEqual(dar_entrenamiento, [], "La lista de entrenamientos no está vacía")


    def test_listar_entrenamiento_con_al_menos_uno(self):

        persona = self.crear_persona_faker()
        self.session.add(Ejercicio(nombre="Estocadas", descripcion="Estocadas por 20 minutos", enlace="https://youtube.com", calorias=250)) 
        self.session.add(Ejercicio(nombre="Sentadilla", descripcion="Sentadilla por 10 minutos", enlace="https://youtube.com", calorias=350))
        self.session.commit()

        # Generar entrenamientos aleatorios con fechas y tiempos generados por Faker
        fecha_random = self.data_factory.date_between(start_date='-10y', end_date='today').strftime('%Y-%m-%d')
        tiempo_random = self.data_factory.time_object().strftime('%H:%M:%S')
        for _ in range(1):
            entrenamiento = Entrenamiento(
                fecha=fecha_random,
                repeticiones=self.data_factory.pyint(0, 100, 1),
                tiempo=tiempo_random,
                persona_id=persona.id,  # Utiliza el ID de la persona
                ejercicio_id=self.data_factory.pyint(1, 2, 1)
            )
            self.session.add(entrenamiento)
        self.session.commit()
        
        # Llama al método para obtener los entrenamientos de la persona
        entrenamiento_en_forma = EntrenamientoEnForma()
        dar_entrenamiento = entrenamiento_en_forma.dar_entrenamientos(persona.id)

        # Ahora puedes realizar las aserciones
        self.assertGreaterEqual(len(dar_entrenamiento), 1, "La lista de entrenamientos no tiene al menos un entrenamiento")

    def crear_persona_faker(self):
        # No necesitas crear otra sesión aquí, utiliza la sesión existente
        nombre = self.data_factory.first_name()
        apellido = self.data_factory.last_name()
        edad = self.data_factory.random_int(min=18, max=100)
        talla = round(self.data_factory.random_int(min=0, max=100), 2)
        peso = round(self.data_factory.random_int(min=0, max=100), 1)
        brazo = round(self.data_factory.random_int(min=0, max=100), 1)
        pecho = round(self.data_factory.random_int(min=0, max=100), 1)
        cintura = round(self.data_factory.random_int(min=0, max=100), 1)
        pierna = round(self.data_factory.random_int(min=0, max=100), 1)
        
        nueva_persona = Persona(
            nombre=nombre,
            apellido=apellido,
            edad=edad,
            talla=talla,
            peso=peso,
            brazo=brazo,
            pecho=pecho,
            cintura=cintura,
            pierna=pierna,
        )

        try:
            self.session.add(nueva_persona)  # Utiliza la sesión existente
            self.session.commit()
            return nueva_persona  # Devuelve la persona creada
        except Exception as e:
            self.session.rollback()
            return None

    def test_listar_entrenamiento_ordenadamente(self):
        # Asegurémonos de que haya una persona y ejercicios para asociar con los entrenamientos
        persona = self.crear_persona_faker()
        self.session.add(Ejercicio(nombre="Estocadas", descripcion="Estocadas por 20 minutos", enlace="https://youtube.com", calorias=250)) 
        self.session.add(Ejercicio(nombre="Sentadilla", descripcion="Sentadilla por 10 minutos", enlace="https://youtube.com", calorias=350))
        self.session.commit()

        # Generar entrenamientos aleatorios con fechas y tiempos generados por Faker
        fecha_random = self.data_factory.date_between(start_date='-10y', end_date='today').strftime('%Y-%m-%d')
        tiempo_random = self.data_factory.time_object().strftime('%H:%M:%S')
        for _ in range(3):
            entrenamiento = Entrenamiento(
                fecha=fecha_random,
                repeticiones=self.data_factory.pyint(0, 100, 1),
                tiempo=tiempo_random,
                persona_id=persona.id,  # Utiliza el ID de la persona
                ejercicio_id=self.data_factory.pyint(1, 2, 1)
            )
            self.session.add(entrenamiento)
        self.session.commit()

        # Obtener los entrenamientos y ordenarlos por fecha (en orden descendente), ejercicio y tiempo
        dar_entrenamiento = EntrenamientoEnForma().dar_entrenamientos(persona.id)  # Utiliza el ID de la persona
        sorted_list = sorted(dar_entrenamiento, key=lambda x: (-int(x["fecha"].replace("-", "")), x["ejercicio"], x["tiempo"]))

        # Verificar que la lista de entrenamientos esté ordenada
        self.assertEqual(dar_entrenamiento, sorted_list, "La lista de entrenamientos no está ordenada correctamente")