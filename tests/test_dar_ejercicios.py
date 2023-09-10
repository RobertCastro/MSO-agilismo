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

        self.session.add(Ejercicio(nombre="Correr", descripcion="Correr por 20 minutos", enlace="https://youtube.com", calorias=200)) 
        self.session.commit()   

        entrenamiento_en_forma = EntrenamientoEnForma()
        dar_ejercicios = entrenamiento_en_forma.dar_ejercicios()
        self.assertEqual(dar_ejercicios, [], "La base de datos no está vacía")
