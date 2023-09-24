import unittest
from faker import Faker
from src.logica.EntrenamientoEnForma import EntrenamientoEnForma
from src.modelo.declarative_base import Session
from src.modelo.Ejercicio import Ejercicio
from src.modelo.Persona import Persona
from src.modelo.Entrenamiento import Entrenamiento
import random

class TestDarReporte(unittest.TestCase):

    def setUp(self):
        self.faker = Faker()
        self.session = Session()
        self.en_forma = EntrenamientoEnForma()
        
        self.persona = Persona(
            nombre=self.faker.first_name(),
            apellido=self.faker.last_name(),
            edad=self.faker.random_int(min=18, max=100),
            talla=round(random.uniform(1.5, 2.0), 2),
            peso=round(random.uniform(50, 100), 2),
            brazo=round(random.uniform(20, 40), 2),
            pecho=round(random.uniform(80, 120), 2),
            cintura=round(random.uniform(60, 100), 2),
            pierna=round(random.uniform(50, 80), 2),
            fecha_inicio=self.faker.date(),
            estado=True
        )
        

        self.ejercicio = Ejercicio(
            nombre=self.faker.name(),
            descripcion=self.faker.text(),
            enlace=self.faker.url(),
            calorias=self.faker.random_int(min=50, max=500)
        )
        self.session.add(self.persona)
        self.session.add(self.ejercicio) 
        self.session.commit()

        self.entrenamiento = Entrenamiento(
            fecha=self.faker.date(),
            repeticiones=self.faker.random_int(min=5, max=50),
            tiempo=self.faker.time(),
            persona_id=self.persona.id,
            ejercicio_id=self.ejercicio.id
        )
        self.session.add(self.entrenamiento)
        self.session.commit()


    def test_calcular_imc(self):
        respuesta = self.en_forma.calcularIMC(self.persona.talla, self.persona.peso)
        self.assertNotEqual(respuesta, "", "Error en el cálculo del IMC")

    def tearDown(self):
        self.session.query(Persona).filter(Persona.id == self.persona.id).delete()
        self.session.commit()
        self.session.close()
