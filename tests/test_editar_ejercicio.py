import unittest
from faker import Faker
import re
from src.logica.EntrenamientoEnForma import EntrenamientoEnForma
from src.modelo.declarative_base import Session
from src.modelo.Ejercicio import Ejercicio
import sys

class TestEditarEjercicio(unittest.TestCase):

    def setUp(self):
        self.faker = Faker()
        self.session = Session()
        self.entrenamiento_en_forma = EntrenamientoEnForma()

    def tearDown(self):
        self.session.query(Ejercicio).delete()
        self.session.commit()
    
    def test_editar_ejercicio_existente(self):
        # Crear un ejercicio de prueba
        ejercicio = Ejercicio(
            nombre=self.faker.name(),
            descripcion=self.faker.text(),
            enlace=self.faker.url(),
            calorias=self.faker.random_int(min=10, max=500)
        )
        self.session.add(ejercicio)
        self.session.commit()

        # Editar el ejercicio
        nuevo_nombre = self.faker.name()
        nuevo_descripcion = self.faker.text()
        nuevo_enlace = self.faker.url()
        nuevo_calorias = self.faker.random_int(min=10, max=500)

        result = self.entrenamiento_en_forma.editar_ejercicio(id_ejercicio=999, nombre=nuevo_nombre, descripcion=nuevo_descripcion, enlace=nuevo_enlace, calorias=nuevo_calorias)

        self.assertEqual(result, "", "El ejercicio no existe")
    




    