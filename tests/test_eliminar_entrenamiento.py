import unittest
from src.modelo.Persona import Persona
from src.modelo.Ejercicio import Ejercicio
from src.logica.EntrenamientoEnForma import EntrenamientoEnForma
from src.modelo.declarative_base import Session
from src.modelo.Entrenamiento import Entrenamiento
from faker import Faker
import random
from datetime import datetime

class TestEliminarEntrenamiento(unittest.TestCase):
    
    def setUp(self): 
        self.EntrenamientoEnForma = EntrenamientoEnForma() 
        self.data_factory = Faker()
        Faker.seed(1000)
        self.session = Session()
        
        # Eliminar todos los datos de entrenamiento, personas y ejercicios en la base de datos
        self.session.query(Entrenamiento).delete()
        self.session.query(Persona).delete()
        self.session.query(Ejercicio).delete()
        self.session.commit()
        self.session.close()

    def crear_persona_faker(self):
            # No necesitas crear otra sesión aquí, utiliza la sesión existente
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
                self.session.add(nueva_persona)  # Utiliza la sesión existente
                self.session.commit()
                return nueva_persona  # Devuelve la persona creada
            except Exception as e:
                self.session.rollback()
                return None

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
        
    def crear_entrenamiento_faker(self, persona_id, ejercicio_id):
        # Genera un entrenamiento falso para la persona y el ejercicio
        fecha_random = self.data_factory.date_between(start_date='-10y', end_date='today').strftime('%Y-%m-%d')
        tiempo_random = self.data_factory.time_object().strftime('%H:%M:%S')
        entrenamiento = Entrenamiento(
            fecha=fecha_random,
            repeticiones=self.data_factory.pyint(0, 100, 1),
            tiempo=tiempo_random,
            persona_id=persona_id,
            ejercicio_id=ejercicio_id
        )
        self.session.add(entrenamiento)
        self.session.commit()
        return entrenamiento
            
    def test_eliminar_entrenamiento(self):
        # Crear una persona y un ejercicio
        persona = self.crear_persona_faker()
        ejercicio = self.crear_ejercicio_faker()
        
        # Generar un entrenamiento para la persona y el ejercicio
        entrenamiento = self.crear_entrenamiento_faker(persona.id, ejercicio.id)

        # Asegurarse de que el entrenamiento existe
        entrenamiento_en_forma = EntrenamientoEnForma()
        entrenamientos_antes = entrenamiento_en_forma.dar_entrenamientos(persona.id)
        self.assertEqual(len(entrenamientos_antes), 1, "La lista de entrenamientos no tiene el entrenamiento antes de eliminarlo")

        # Eliminar el entrenamiento
        entrenamiento_en_forma.eliminar_entrenamiento(entrenamiento.id)

        # Intentar obtener el entrenamiento eliminado
        entrenamientos_despues = entrenamiento_en_forma.dar_entrenamientos(persona.id)

        # Verificar que el entrenamiento haya sido eliminado
        self.assertEqual(len(entrenamientos_despues), 0, "El entrenamiento no se ha eliminado correctamente")

    def test_eliminar_entrenamiento_inexistente(self):
        # Crear una persona y un ejercicio
        persona = self.crear_persona_faker()
        ejercicio = self.crear_ejercicio_faker()
        
        # Intentar eliminar un entrenamiento que no existe
        entrenamiento_en_forma = EntrenamientoEnForma()
        entrenamiento_id_inexistente = 12345  # Un ID que sabemos que no existe
        entrenamiento_en_forma.eliminar_entrenamiento(entrenamiento_id_inexistente)

        # Intentar obtener el entrenamiento eliminado
        entrenamientos_despues = entrenamiento_en_forma.dar_entrenamientos(persona.id)

        # Verificar que no se haya eliminado ningún entrenamiento
        self.assertEqual(len(entrenamientos_despues), 0, "No debería haber entrenamientos eliminados")






