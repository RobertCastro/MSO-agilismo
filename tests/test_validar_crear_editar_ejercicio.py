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

    def test_validar_crear_editar_ejercicio_longitud_maxima_nombre(self):

        nombre_largo = "z" * 201
        entrenamiento_en_forma = EntrenamientoEnForma()
        resultado = entrenamiento_en_forma.validar_crear_editar_ejercicio(nombre_largo, "Descripción", "https://enlace.com", 200)
        self.assertNotEqual(resultado, "", "El nombre excede los 200 caracteres")

    def test_validar_crear_editar_ejercicio_longitud_maxima_descripcion(self):

        descripcion_larga = "a" * 201
        entrenamiento_en_forma = EntrenamientoEnForma()
        resultado = entrenamiento_en_forma.validar_crear_editar_ejercicio("Correr", descripcion_larga, "https://enlace.com", 200)
        self.assertNotEqual(resultado, "", "La descripción excede los 200 caracteres")

    def test_validar_crear_editar_ejercicio_nombre_solo_alfanumerico(self):

        entrenamiento_en_forma = EntrenamientoEnForma()
        resultado = entrenamiento_en_forma.validar_crear_editar_ejercicio("Correr!", "descripcion", "https://enlace.com", 200)
        self.assertNotEqual(resultado, "", "El nombre tiene caracteres no alfanumericos")

    def test_validar_crear_editar_ejercicio_descripcion_solo_alfanumerico(self):

        entrenamiento_en_forma = EntrenamientoEnForma()
        resultado = entrenamiento_en_forma.validar_crear_editar_ejercicio("Correr", "descripcion!", "https://enlace.com", 200)
        self.assertNotEqual(resultado, "", "La descripción tiene caracteres no alfanumericos")

    def test_validar_crear_editar_ejercicio_url_invalida(self):
        entrenamiento_en_forma = EntrenamientoEnForma()
        
        resultado = entrenamiento_en_forma.validar_crear_editar_ejercicio("Nombre", "Descripción", "no es una url", 100)
        self.assertEqual(resultado, "", "La URL no era válida.")

