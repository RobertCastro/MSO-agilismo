import unittest
from src.modelo.Persona import Persona
from src.modelo.Ejercicio import Ejercicio
from src.logica.EntrenamientoEnForma import EntrenamientoEnForma
from src.modelo.declarative_base import Session
from src.modelo.Entrenamiento import Entrenamiento
from faker import Faker
import random
from datetime import datetime

class TestValidarCrearEntrenamiento(unittest.TestCase):
    
    def setUp(self): 
        self.EntrenamientoEnForma = EntrenamientoEnForma() 
        self.data_factory = Faker()
        Faker.seed(1000)
        self.session = Session()
        
        entrenamientos = self.session.query(Entrenamiento).all() 
        for entrenamiento in entrenamientos: 
            self.session.delete(entrenamiento) 
            self.session.commit() 

        personas = self.session.query(Persona).all() 
        for persona in personas: 
            self.session.delete(persona) 
            self.session.commit() 
            self.session.close() 

        ejercicios = self.session.query(Ejercicio).all() 
        for ejercicio in ejercicios: 
            self.session.delete(ejercicio) 
            self.session.commit() 

        self.session.close()
        
    def tearDown(self): 
        entrenamientos = self.session.query(Entrenamiento).all() 
        for entrenamiento in entrenamientos: 
            self.session.delete(entrenamiento) 
            self.session.commit() 

        personas = self.session.query(Persona).all() 
        for persona in personas: 
            self.session.delete(persona) 
            self.session.commit() 
            self.session.close() 

        ejercicios = self.session.query(Ejercicio).all() 
        for ejercicio in ejercicios: 
            self.session.delete(ejercicio) 
            self.session.commit() 

        self.session.close()
    
    def crear_persona_faker(self):

        session = Session()
        
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
            session.add(nueva_persona)
            session.commit()
            session.close()
            return nueva_persona
        except Exception as e:
            session.rollback()
            session.close()
            return ""
    
    def crear_ejercicio_faker(self):
        session = Session()
        
        nombre = self.data_factory.unique.first_name()
        descripcion = self.data_factory.text(max_nb_chars=200)
        enlace = self. data_factory.url()
        calorias = random.randint(50, 500)
                
        nuevo_ejercicio = Ejercicio(
            nombre=nombre,
            descripcion=descripcion,
            enlace=enlace,
            calorias=calorias,
        )
        try:
            session.add(nuevo_ejercicio)
            session.commit()
            return nuevo_ejercicio
        except Exception as e:
            session.rollback()
            session.close()
            return ""
     
    
    def test_validar_entrenamiento_ejercicio_vacio(self):
            
        persona = self.crear_persona_faker()
        ejercicio = self.crear_ejercicio_faker()
        
        fecha_random = self.data_factory.date_between(start_date='-10y', end_date='today')
        fecha = fecha_random.strftime('%Y-%m-%d')
        repeticiones = self.data_factory.random_int(min=1, max=100)
        tiempo = self.data_factory.time_object()

        entrenamiento_en_forma = EntrenamientoEnForma()
        resultado = entrenamiento_en_forma.validar_crear_editar_entrenamiento(persona, ejercicio.nombre, fecha, repeticiones, tiempo)
        self.assertNotEqual(resultado, None, "Ejercicio está vacío.")
    
    def test_validar_entrenamiento_fecha_vacio(self):
            
        persona = self.crear_persona_faker()
        ejercicio = self.crear_ejercicio_faker()
        
        fecha_random = self.data_factory.date_between(start_date='-10y', end_date='today')
        fecha = fecha_random.strftime('%Y-%m-%d')
        repeticiones = self.data_factory.random_int(min=1, max=100)
        tiempo = self.data_factory.time_object()

        entrenamiento_en_forma = EntrenamientoEnForma()
        resultado = entrenamiento_en_forma.validar_crear_editar_entrenamiento(persona, ejercicio.nombre, fecha, repeticiones, tiempo)
        print(resultado)
        self.assertNotEqual(resultado, None, "Fecha está vacío.")
    
    def test_validar_entrenamiento_repeticiones_vacio(self):
        
        persona = self.crear_persona_faker()
        ejercicio = self.crear_ejercicio_faker()
        
        repeticiones = self.data_factory.random_int(min=1, max=100)
        fecha = self.data_factory.date_between(start_date='-10y', end_date='today')
        tiempo = self.data_factory.time_object()

        entrenamiento_en_forma = EntrenamientoEnForma()
        resultado = entrenamiento_en_forma.validar_crear_editar_entrenamiento(persona, ejercicio.nombre, fecha, repeticiones, tiempo)
        self.assertNotEqual(resultado, None, "Repeticiones está vacío.")
        
    def test_validar_entrenamiento_tiempo_vacio(self):
        
        persona = self.crear_persona_faker()
        ejercicio = self.crear_ejercicio_faker()
        
        repeticiones = self.data_factory.random_int(min=1, max=100)
        fecha = self.data_factory.date_between(start_date='-10y', end_date='today')
        tiempo = self.data_factory.time_object()

        entrenamiento_en_forma = EntrenamientoEnForma()
        resultado = entrenamiento_en_forma.validar_crear_editar_entrenamiento(persona, ejercicio.nombre, fecha, repeticiones, tiempo)
        self.assertNotEqual(resultado, None, "Tiempo está vacío.")
    
    def test_validar_entrenamiento_repeticiones_positivo(self):
        
        persona = self.crear_persona_faker()
        ejercicio = self.crear_ejercicio_faker()
        
        repeticiones = self.data_factory.random_int(min=1, max=100)
        fecha = self.data_factory.date_between(start_date='-10y', end_date='today')
        tiempo = self.data_factory.time_object()

        entrenamiento_en_forma = EntrenamientoEnForma()
        resultado = entrenamiento_en_forma.validar_crear_editar_entrenamiento(persona, ejercicio.nombre, fecha, repeticiones, tiempo)
        self.assertNotEqual(resultado, None, "Repeticiones deben ser un número entero positivo")
    
    def test_validar_entrenamiento_formato_tiempo(self):
        
        persona = self.crear_persona_faker()
        ejercicio = self.crear_ejercicio_faker()
        tiempo = self.data_factory.time_object()
        repeticiones = self.data_factory.random_int(min=1, max=100)
        fecha = self.data_factory.date_between(start_date='-10y', end_date='today')

        entrenamiento_en_forma = EntrenamientoEnForma()
        resultado = entrenamiento_en_forma.validar_crear_editar_entrenamiento(persona, ejercicio.nombre, fecha, repeticiones, tiempo)
        self.assertNotEqual(resultado, None, "Tiempo no tiene el formato correcto (hh:mm:ss)")
    
    def test_validar_entrenamiento_formato_fecha(self):
        
        persona = self.crear_persona_faker()
        ejercicio = self.crear_ejercicio_faker()
        tiempo = self.data_factory.time_object()
        repeticiones = self.data_factory.random_int(min=1, max=100)
        fecha_random = self.data_factory.date_between(start_date='-10y', end_date='today')
        fecha = fecha_random.strftime('%Y-%m-%d')

        entrenamiento_en_forma = EntrenamientoEnForma()
        resultado = entrenamiento_en_forma.validar_crear_editar_entrenamiento(persona, ejercicio.nombre, fecha, repeticiones, tiempo)
        self.assertNotEqual(resultado, None, "Fecha no tiene el formato correcto (aaaa-mm-dd)")
