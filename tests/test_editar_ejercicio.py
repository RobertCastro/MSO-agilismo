import unittest
from faker import Faker
from src.logica.EntrenamientoEnForma import EntrenamientoEnForma
from src.modelo.declarative_base import Session
from src.modelo.Ejercicio import Ejercicio

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

        result = self.entrenamiento_en_forma.editar_ejercicio(id_ejercicio=ejercicio.id, nombre=nuevo_nombre, descripcion=nuevo_descripcion, enlace=nuevo_enlace, calorias=nuevo_calorias)

        self.assertEqual(result, "", "El ejercicio no existe")
    
    def test_editar_ejercicio_nombre_igual(self):
        nombre = self.faker.unique.name()
        descripcion = self.faker.text(max_nb_chars=200)
        enlace = self.faker.url()
        calorias = self.faker.random_int(min=50, max=500)
        
        entrenamiento_en_forma = EntrenamientoEnForma()
        
        nuevo_ejercicio = Ejercicio(
            nombre=nombre,
            descripcion=descripcion,
            enlace=enlace,
            calorias=calorias
        )
        
        self.session.add(nuevo_ejercicio) 
        self.session.commit()

        resultado = entrenamiento_en_forma.validar_ejercicio_existente(id_ejercicio=nuevo_ejercicio.id, nombre=nuevo_ejercicio.nombre)
        self.assertEqual(resultado, "", "La validación detectó un ejercicio duplicado.")



    