import unittest
from faker import Faker
from src.logica.EntrenamientoEnForma import EntrenamientoEnForma
from src.modelo.declarative_base import Session
from src.modelo.Ejercicio import Ejercicio

class TestDarEjercicios(unittest.TestCase):
    def setUp(self):

        self.session = Session()
        self.session.query(Ejercicio).delete()  
        self.session.commit()
        
        self.data_factory = Faker()
        Faker.seed(1000)
        
    def tearDown(self):
        self.session.query(Ejercicio).delete()  
        self.session.commit()

    def test_listar_ejercicios_vacia(self):

        self.session.query(Ejercicio).delete()
        self.session.commit() 
  
        entrenamiento_en_forma = EntrenamientoEnForma()
        dar_ejercicios = entrenamiento_en_forma.dar_ejercicios()
        self.assertFalse(dar_ejercicios)

    def test_listar_ejercicios_con_al_menos_uno(self):
 
        for _ in range(2):
            nombre = self.data_factory.unique.name()
            descripcion = self.data_factory.text(max_nb_chars=200)
            enlace = self.data_factory.url()
            calorias = self.data_factory.random_int(min=50, max=500)
            
            ejercicio = Ejercicio(nombre=nombre, descripcion=descripcion, enlace=enlace, calorias=calorias)
            self.session.add(ejercicio)
        self.session.commit()  
             
        entrenamiento_en_forma = EntrenamientoEnForma()
        dar_ejercicios = entrenamiento_en_forma.dar_ejercicios()
        self.assertNotEqual(dar_ejercicios, [], "La lista de ejercicios tiene al menos un ejercicio")

    def test_listar_ejercicios_por_nombre(self):
        
        for _ in range(20):
            nombre = self.data_factory.unique.name()
            descripcion = self.data_factory.text(max_nb_chars=200)
            enlace = self.data_factory.url()
            calorias = self.data_factory.random_int(min=50, max=500)
            
            ejercicio = Ejercicio(nombre=nombre, descripcion=descripcion, enlace=enlace, calorias=calorias)
            self.session.add(ejercicio)
        self.session.commit()

        entrenamiento_en_forma = EntrenamientoEnForma()
        dar_ejercicios = entrenamiento_en_forma.dar_ejercicios()
        nombre = [(ejercicio['nombre']) for ejercicio in dar_ejercicios]
        self.assertEqual(nombre, sorted(nombre), "La lista de ejercicios no está ordenada correctamente")

