from src.logica.FachadaEnForma import FachadaEnForma
from src.modelo.declarative_base import Session
from src.modelo.Persona import Persona
from src.modelo.Ejercicio import Ejercicio

class EntrenamientoEnForma(FachadaEnForma):

    def __init__(self):
        #Constructor necesario para usar interfaz de listado ejercicios y acceder a pantalla crear_ejercicio
        self.ejercicios = [
            {'nombre': 'Press de pierna', 'descripcion': 'Ejercicio de entrenamiento con pesas en el que el individuo empuja un peso o una resistencia con las piernas', 'youtube': 'https://www.youtube.com/watch?v=zac9BPZiUTQ', 'calorias': 120}, \
            {'nombre': 'Sentadilla', 'descripcion': 'Ejercicio de fuerza en el que se baja la cadera desde una posición de pie y luego vuelve a levantarse.', 'youtube': 'https://www.youtube.com/watch?v=l7aszLSPCVg', 'calorias': 80}, \
            {'nombre': 'Abducción de cadera', 'descripcion': 'Mover la pierna derecha hacia la derecha o alejarla del cuerpo y viceversa', 'youtube': 'https://www.youtube.com/watch?v=dILxTvY88uI', 'calorias': 90}
        ]


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
        return self.ejercicios.copy()
    def validar_crear_editar_ejercicio(self, nombre, descripcion, enlace, calorias):
        return ""