import unittest
from src.logica.EntrenamientoEnForma import EntrenamientoEnForma
from src.modelo.declarative_base import Session
from src.modelo.Persona import Persona

class TestDarPersonas(unittest.TestCase):

    def setUp(self):

        self.session = Session()
        self.session.query(Persona).delete()  
        self.session.commit()

    def test_base_de_datos_vacia(self):

        self.session.add(Persona(nombre="Test", apellido="User")) 
        self.session.commit()

        entrenamiento_en_forma = EntrenamientoEnForma()
        dar_personas = entrenamiento_en_forma.dar_personas()

        self.assertEqual(dar_personas, [], "La base de datos no está vacía")

