import unittest
from src.logica.EntrenamientoEnForma import EntrenamientoEnForma

class TestDarPersonas(unittest.TestCase):

    def test_base_de_datos_vacia(self):
        entrenamiento_en_forma = EntrenamientoEnForma()
        dar_personas = entrenamiento_en_forma.dar_personas()
        
        self.assertEqual(dar_personas, [], "La base de datos no está vacía")


