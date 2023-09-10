from src.logica.FachadaEnForma import FachadaEnForma
from src.modelo.declarative_base import Session
from src.modelo.Persona import Persona
from src.modelo.Ejercicio import Ejercicio

class EntrenamientoEnForma(FachadaEnForma):


    def dar_personas(self):

        session = Session()
        personas = session.query(Persona).all()
            
        personas_dict = [
            {
                'id': persona.id,
                'nombre': persona.nombre,
                'apellido': persona.apellido,
            }
            for persona in personas
        ]

        session.close()

        return personas_dict
    
    def crear_ejercicio(self, nombre, descripcion, enlace, calorias):
        session = Session()
        nuevo_ejercicio = Ejercicio(
            nombre=nombre,
            descripcion=descripcion,
            enlace=enlace,
            calorias=calorias
        )
        session.add(nuevo_ejercicio)
        session.commit()
        session.close()

    def dar_ejercicios(self):
        session = Session()
        ejercicios = session.query(Ejercicio).all()
            
        ejercicios_dict = [
            {
                'id': ejercicio.id,
                'nombre': ejercicio.nombre,
                'descripcion': ejercicio.descripcion,
                'enlace': ejercicio.enlace,
                'calorias': ejercicio.calorias
            }
            for ejercicio in ejercicios
        ]

        session.close()

        return ejercicios_dict

    def validar_crear_editar_ejercicio(self, nombre, descripcion, enlace, calorias):
        return ""