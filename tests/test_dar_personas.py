import unittest
from src.logica.EntrenamientoEnForma import EntrenamientoEnForma
from src.modelo.declarative_base import Session
from src.modelo.Persona import Persona

class TestDarPersonas(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        session = Session()
        session.query(Persona).delete() 
        session.commit()
        session.close()

    def test_base_de_datos_vacia(self):
        entrenamiento_en_forma = EntrenamientoEnForma()
        dar_personas = entrenamiento_en_forma.dar_personas()
        
        self.assertEqual(dar_personas, [], "La base de datos no está vacía")
    
    def test_base_de_datos_con_una_persona(self):
        entrenamiento_en_forma = EntrenamientoEnForma()
        dar_personas = entrenamiento_en_forma.dar_personas()
        self.assertEqual(len(dar_personas), 1, "La base de datos no contiene exactamente una persona")

