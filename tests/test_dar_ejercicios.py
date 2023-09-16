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
        self.assertEqual(dar_ejercicios, [], "La lista de ejercicios no está vacía")

    def test_listar_ejercicios_con_al_menos_uno(self):

        self.session.add(Ejercicio(nombre="Correr", descripcion="Correr por 20 minutos", enlace="https://youtube.com", calorias=200))
        self.session.add(Ejercicio(nombre="Abdominales", descripcion="Abdominales por 20 minutos", enlace="https://youtube.com", calorias=250)) 
        self.session.commit()        
        entrenamiento_en_forma = EntrenamientoEnForma()
        dar_ejercicios = entrenamiento_en_forma.dar_ejercicios()
        self.assertGreaterEqual(len(dar_ejercicios), 1, "La lista de ejercicios tiene al menos un ejercicio")

    def test_listar_ejercicios_por_nombre(self):

        self.session.add(Ejercicio(nombre="Correr", descripcion="Correr por 20 minutos", enlace="https://youtube.com", calorias=200))
        self.session.add(Ejercicio(nombre="Abdominales", descripcion="Abdominales por 20 minutos", enlace="https://youtube.com", calorias=250)) 
        self.session.add(Ejercicio(nombre="Sentadilla", descripcion="Sentadilla por 10 minutos", enlace="https://youtube.com", calorias=350)) 
        self.session.add(Ejercicio(nombre="Estocadas", descripcion="Estocadas por 20 minutos", enlace="https://youtube.com", calorias=250)) 
        self.session.commit()

        entrenamiento_en_forma = EntrenamientoEnForma()
        dar_ejercicios = entrenamiento_en_forma.dar_ejercicios()
        nombre = [(ejercicio['nombre']) for ejercicio in dar_ejercicios]
        self.assertEqual(nombre, sorted(nombre), "La lista de ejercicios no está ordenada correctamente")

