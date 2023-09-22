import unittest
from faker import Faker
import random
from src.logica.EntrenamientoEnForma import EntrenamientoEnForma
from src.modelo.declarative_base import Session
from src.modelo.Persona import Persona

class TestDarPersonas(unittest.TestCase):

    def setUp(self):

        self.session = Session()
        self.session.query(Persona).delete()  
        self.session.commit()
        
        self.data_factory = Faker()
        Faker.seed(1000)
        
        for _ in range(5):
            nueva_persona = Persona(
                nombre=self.data_factory.first_name(),
                apellido=self.data_factory.last_name(),
                edad=round(random.randint(18, 80), 1),
                talla=round(random.uniform(1.40, 2.00), 1),
                peso=round(random.uniform(40.0, 180.0), 1),
                brazo=round(random.uniform(20.0, 35.0), 1),
                pecho=round(random.uniform(70.0, 120.0), 1),
                cintura=round(random.uniform(60.0, 100.0), 1),
                pierna=round(random.uniform(50.0, 80.0), 1),
            )
            self.session.add(nueva_persona)
        self.session.commit()
    
    def tearDown(self):
        self.session.query(Persona).delete()  
        self.session.commit()

    def test_listar_personas_vacia(self):

        self.session.query(Persona).delete()  
        self.session.commit()

        entrenamiento_en_forma = EntrenamientoEnForma()
        dar_personas = entrenamiento_en_forma.dar_personas()

        self.assertEqual(dar_personas, [], "La base de datos no está vacía")

    def test_listar_personas__con_al_menos_una_persona(self):

        for _ in range(5):
            nueva_persona = Persona(
                nombre=self.data_factory.first_name(),
                apellido=self.data_factory.last_name(),
                edad=round(random.randint(18, 80), 1),
                talla=round(random.uniform(1.40, 2.00), 1),
                peso=round(random.uniform(40.0, 180.0), 1),
                brazo=round(random.uniform(20.0, 35.0), 1),
                pecho=round(random.uniform(70.0, 120.0), 1),
                cintura=round(random.uniform(60.0, 100.0), 1),
                pierna=round(random.uniform(50.0, 80.0), 1),
            )
            self.session.add(nueva_persona)
        self.session.commit()

        entrenamiento_en_forma = EntrenamientoEnForma()
        dar_personas = entrenamiento_en_forma.dar_personas()
        self.assertGreaterEqual(len(dar_personas), 1, "La base de datos contiene al menos una persona")

    def test_personas_ordenadas_por_nombre_y_apellido(self):

        for _ in range(20):
            nueva_persona = Persona(
                nombre=self.data_factory.first_name(),
                apellido=self.data_factory.last_name(),
                edad=round(random.randint(18, 80), 1),
                talla=round(random.uniform(1.40, 2.00), 1),
                peso=round(random.uniform(40.0, 180.0), 1),
                brazo=round(random.uniform(20.0, 35.0), 1),
                pecho=round(random.uniform(70.0, 120.0), 1),
                cintura=round(random.uniform(60.0, 100.0), 1),
                pierna=round(random.uniform(50.0, 80.0), 1),
            )
            self.session.add(nueva_persona)
        self.session.commit()

        entrenamiento_en_forma = EntrenamientoEnForma()
        dar_personas = entrenamiento_en_forma.dar_personas()
        nombres_apellidos = [(persona['nombre'], persona['apellido']) for persona in dar_personas]
        self.assertEqual(nombres_apellidos, sorted(nombres_apellidos), "La lista de personas no está ordenada correctamente por nombre y apellido")

