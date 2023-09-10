import unittest
from src.logica.EntrenamientoEnForma import EntrenamientoEnForma
from src.modelo.declarative_base import Session
from src.modelo.Ejercicio import Ejercicio

class TestDarEjercicios(unittest.TestCase):

    def setUp(self):

        self.session = Session()
        self.session.query(Ejercicio).delete()  
        self.session.commit()

    def test_listar_ejercicios_vacia(self):  

        entrenamiento_en_forma = EntrenamientoEnForma()
        dar_ejercicios = entrenamiento_en_forma.dar_ejercicios()
        self.assertEqual(dar_ejercicios, [], "La base de datos no está vacía")

    def test_listar_ejercicios_con_al_menos_uno(self):

        entrenamiento_en_forma = EntrenamientoEnForma()
        dar_ejercicios = entrenamiento_en_forma.dar_ejercicios()
        self.assertGreaterEqual(len(dar_ejercicios), 1, "La base de datos contiene al menos una persona")
