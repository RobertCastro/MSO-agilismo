import unittest
from src.logica.EntrenamientoEnForma import EntrenamientoEnForma
from src.modelo.declarative_base import Session
from src.modelo.Persona import Persona

class TestDarPersonas(unittest.TestCase):

    def setUp(self):

        self.session = Session()
        self.session.query(Persona).delete()  
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

        self.session.add(Persona(nombre="Test", apellido="User")) 
        self.session.add(Persona(nombre="Test2", apellido="User2")) 
        self.session.commit()

        entrenamiento_en_forma = EntrenamientoEnForma()
        dar_personas = entrenamiento_en_forma.dar_personas()
        self.assertGreaterEqual(len(dar_personas), 1, "La base de datos contiene al menos una persona")

    def test_personas_ordenadas_por_nombre_y_apellido(self):

        self.session.add(Persona(nombre="Carlos", apellido="Gomez"))
        self.session.add(Persona(nombre="Ana", apellido="Perez"))
        self.session.add(Persona(nombre="Zack", apellido="Lopez"))
        self.session.add(Persona(nombre="Beto", apellido="Zapata"))
        self.session.commit()

        entrenamiento_en_forma = EntrenamientoEnForma()
        dar_personas = entrenamiento_en_forma.dar_personas()
        nombres_apellidos = [(persona['nombre'], persona['apellido']) for persona in dar_personas]
        self.assertEqual(nombres_apellidos, sorted(nombres_apellidos), "La lista de personas no está ordenada correctamente por nombre y apellido")

