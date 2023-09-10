import unittest
from src.logica.EntrenamientoEnForma import EntrenamientoEnForma
from src.modelo.declarative_base import Session
from src.modelo.Persona import Persona

class TestValidarCrearEditarEjercicio(unittest.TestCase):

    def test_validar_crear_editar_ejercicio_nombre_vacio(self):
        entrenamiento_en_forma = EntrenamientoEnForma()
        resultado = entrenamiento_en_forma.validar_crear_editar_ejercicio("", "Descripción", "https://enlace.com", 100)
        self.assertNotEqual(resultado, "", "Nombre está vacío.")

    def test_validar_crear_editar_ejercicio_descripcion_vacia(self):
        entrenamiento_en_forma = EntrenamientoEnForma()
        resultado = entrenamiento_en_forma.validar_crear_editar_ejercicio("Nombre", "", "https://enlace.com", 100)
        self.assertNotEqual(resultado, "", "Descripción está vacía.")

    def test_validar_crear_editar_ejercicio_enlace_vacio(self):
        entrenamiento_en_forma = EntrenamientoEnForma()
        resultado = entrenamiento_en_forma.validar_crear_editar_ejercicio("Nombre", "Descripción", "", 100)
        self.assertNotEqual(resultado, "", "Enlace está vacío.")

    def test_validar_crear_editar_ejercicio_calorias_vacias(self):
        entrenamiento_en_forma = EntrenamientoEnForma()
        resultado = entrenamiento_en_forma.validar_crear_editar_ejercicio("Nombre", "Descripción", "https://enlace.com", None)
        self.assertNotEqual(resultado, "", "Calorías están vacías.")


