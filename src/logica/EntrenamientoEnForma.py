from src.logica.FachadaEnForma import FachadaEnForma
from src.modelo.declarative_base import Session
from src.modelo.Persona import Persona
from src.modelo.Ejercicio import Ejercicio
import re

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
        ejercicios = session.query(Ejercicio).order_by(Ejercicio.nombre.asc()).all()
            
        ejercicios_dict = [
            {
                'id': ejercicio.id,
                'nombre': re.sub(r'\W+', '', ejercicio.nombre)[:200],
                'descripcion': ejercicio.descripcion,
                'enlace': ejercicio.enlace,
                'calorias': ejercicio.calorias
            }
            for ejercicio in ejercicios
        ]

        session.close()

        return ejercicios_dict

    def validar_crear_editar_ejercicio(self, nombre, descripcion, enlace, calorias):
        if not nombre or not descripcion or not enlace or calorias is None:
            return "Complete todos los campos"
        if len(nombre) > 200:   
            return "La extensión max de caracteres del nombre debe ser 200"
        if len(descripcion) > 200:   
            return "La extensión max de caracteres de la descripcion debe ser 200"
        if not nombre.isalnum():
            return "El nombre solo debe contener caracteres alfanuméricos"
        return ""