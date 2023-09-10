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

        self.session.add(Ejercicio(nombre="Correr", descripcion="Correr por 20 minutos", enlace="https://youtube.com", calorias=200))
        self.session.add(Ejercicio(nombre="Abdominales", descripcion="Abdominales por 20 minutos", enlace="https://youtube.com", calorias=250)) 
        self.session.commit()

        entrenamiento_en_forma = EntrenamientoEnForma()
        dar_ejercicios = entrenamiento_en_forma.dar_ejercicios()
        self.assertGreaterEqual(len(dar_ejercicios), 1, "La base de datos contiene al menos una persona")

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

    def test_nombre_solo_alfanumerico(self):
        ejercicio_no_valido = Ejercicio(nombre="Correr!", descripcion="Correr por 20 minutos", enlace="https://youtube.com", calorias=200)
        self.session.add(ejercicio_no_valido)
        self.session.commit()

        entrenamiento_en_forma = EntrenamientoEnForma()
        ejercicios = entrenamiento_en_forma.dar_ejercicios()

        for ejercicio in ejercicios:
            self.assertTrue(ejercicio['nombre'].isalnum(), f"El nombre del ejercicio '{ejercicio['nombre']}' no es alfanumérico")

    def test_dar_ejercicios_longitud_maxima_nombre(self):

        nombre_largo = "z" * 201
        ejercicio_nombre_largo = Ejercicio(nombre=nombre_largo, descripcion="Descripción", enlace="https://youtube.com", calorias=200)
        self.session.add(ejercicio_nombre_largo)
        self.session.commit()

        entrenamiento_en_forma = EntrenamientoEnForma()
        ejercicios = entrenamiento_en_forma.dar_ejercicios()

        for ejercicio in ejercicios:
            self.assertTrue(len(ejercicio['nombre']) <= 200, f"El nombre del ejercicio '{ejercicio['nombre']}' excede los 200 caracteres")




