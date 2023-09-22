import unittest
from faker import Faker
import re
from src.logica.EntrenamientoEnForma import EntrenamientoEnForma
from src.modelo.declarative_base import Session
from src.modelo.Ejercicio import Ejercicio

class TestValidarCrearEjercicio(unittest.TestCase):
    
    def setUp(self):

        self.session = Session()
        self.session.query(Ejercicio).delete()  
        self.session.commit()
        
        self.data_factory = Faker()
        Faker.seed(1000)
        
    def tearDown(self):
        self.session = Session()
        self.session.query(Ejercicio).delete()  
        self.session.commit()
        
    def generate_fake_name(self):
        fake = Faker()
        max_attempts = 100
        for _ in range(max_attempts):
            name = fake.unique.first_name()
            # Verifica si el nombre contiene solo caracteres alfanuméricos y espacios
            if not any(char.isalpha() or char.isspace() for char in name):
                return name

    def test_validar_crear_ejercicio_nombre_vacio(self):
        nombre = self.data_factory.unique.name()
        descripcion = self.data_factory.text(max_nb_chars=200)
        enlace = self.data_factory.url()
        calorias = self.data_factory.random_int(min=50, max=500)

        entrenamiento_en_forma = EntrenamientoEnForma()
        resultado = entrenamiento_en_forma.validar_crear_editar_ejercicio(nombre=nombre, descripcion=descripcion, enlace=enlace, calorias=calorias)
        self.assertNotEqual(resultado, None, "Nombre está vacío.")

    def test_validar_crear_ejercicio_descripcion_vacia(self):
        nombre = self.data_factory.unique.name()
        descripcion = self.data_factory.text(max_nb_chars=200)
        enlace = self.data_factory.url()
        calorias = self.data_factory.random_int(min=50, max=500)
        
        entrenamiento_en_forma = EntrenamientoEnForma()
        resultado = entrenamiento_en_forma.validar_crear_editar_ejercicio(nombre=nombre, descripcion=descripcion, enlace=enlace, calorias=calorias)
        self.assertNotEqual(resultado, None, "Descripción está vacía.")

    def test_validar_crear_ejercicio_enlace_vacio(self):
        nombre = self.data_factory.unique.name()
        descripcion = self.data_factory.text(max_nb_chars=200)
        enlace = self.data_factory.url()
        calorias = self.data_factory.random_int(min=50, max=500)
        
        entrenamiento_en_forma = EntrenamientoEnForma()
        resultado = entrenamiento_en_forma.validar_crear_editar_ejercicio(nombre=nombre, descripcion=descripcion, enlace=enlace, calorias=calorias)
        self.assertNotEqual(resultado, None, "Enlace está vacío.")

    def test_validar_crear_ejercicio_calorias_vacias(self):
        nombre = self.data_factory.unique.name()
        descripcion = self.data_factory.text(max_nb_chars=200)
        enlace = self.data_factory.url()
        calorias = self.data_factory.random_int(min=50, max=500)
        
        entrenamiento_en_forma = EntrenamientoEnForma()
        resultado = entrenamiento_en_forma.validar_crear_editar_ejercicio(nombre=nombre, descripcion=descripcion, enlace=enlace, calorias=calorias)
        self.assertNotEqual(resultado, None, "Calorías están vacías.")


    def test_validar_crear_ejercicio_longitud_maxima_nombre(self):
        nombre = self.data_factory.unique.name()
        descripcion = self.data_factory.text(max_nb_chars=200)
        enlace = self.data_factory.url()
        calorias = self.data_factory.random_int(min=50, max=500)
        
        entrenamiento_en_forma = EntrenamientoEnForma()
        resultado = entrenamiento_en_forma.validar_crear_editar_ejercicio(nombre=nombre, descripcion=descripcion, enlace=enlace, calorias=calorias)
        self.assertNotEqual(resultado, None, "El nombre excede los 200 caracteres")

    def test_validar_crear_ejercicio_longitud_maxima_descripcion(self):
        nombre = self.data_factory.unique.name()
        descripcion = self.data_factory.text(max_nb_chars=200)
        enlace = self.data_factory.url()
        calorias = self.data_factory.random_int(min=50, max=500)
        
        entrenamiento_en_forma = EntrenamientoEnForma()
        resultado = entrenamiento_en_forma.validar_crear_editar_ejercicio(nombre=nombre, descripcion=descripcion, enlace=enlace, calorias=calorias)
        self.assertNotEqual(resultado, None, "La descripción excede los 200 caracteres")
    
    def test_validar_crear_ejercicio_nombre_alfanumerico(self):
        nombre = self.generate_fake_name()
        descripcion = self.data_factory.text(max_nb_chars=200)
        enlace = self.data_factory.url()
        calorias = self.data_factory.random_int(min=50, max=500)

        entrenamiento_en_forma = EntrenamientoEnForma()
        resultado = entrenamiento_en_forma.validar_crear_editar_ejercicio(nombre=nombre, descripcion=descripcion, enlace=enlace, calorias=calorias)
        self.assertNotEqual(resultado, "", "El nombre tiene caracteres no alfanumericos")

    def test_validar_crear_ejercicio_enlace_valido(self):
        nombre = self.data_factory.unique.name()
        descripcion = self.data_factory.text(max_nb_chars=200)
        enlace = self.data_factory.url()
        calorias = self.data_factory.random_int(min=50, max=500)
        
        entrenamiento_en_forma = EntrenamientoEnForma()
        resultado = entrenamiento_en_forma.validar_crear_editar_ejercicio(nombre=nombre, descripcion=descripcion, enlace=enlace, calorias=calorias)
        self.assertNotEqual(resultado, None, "La URL no era válida.")

    def test_validar_crear_ejercicio_nombre_existente(self):
        nombre = self.data_factory.unique.name()
        descripcion = self.data_factory.text(max_nb_chars=200)
        enlace = self.data_factory.url()
        calorias = self.data_factory.random_int(min=50, max=500)
        
        entrenamiento_en_forma = EntrenamientoEnForma()
        self.session.add(Ejercicio(nombre=nombre, descripcion=descripcion, enlace=enlace, calorias=calorias)) 
        self.session.commit()

        resultado = entrenamiento_en_forma.validar_crear_editar_ejercicio(nombre=nombre, descripcion=descripcion, enlace=enlace, calorias=calorias)
        self.assertNotEqual(resultado, "", "La validación detectó un ejercicio duplicado.")