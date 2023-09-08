from src.logica.FachadaEnForma import FachadaEnForma
from src.modelo.declarative_base import Session
from src.modelo.Persona import Persona
from datetime import datetime


class EntrenamientoEnForma(FachadaEnForma):

    def __init__(self):
        #Este constructor contiene los datos falsos para probar la interfaz
        self.personas = [{'nombre': 'Federico', 'apellido': 'Contreras', 'edad': 15, 'talla': 1.53, 'peso': 50, 'brazo': 15, 'pecho': 80, 'cintura': 70, 'pierna': 35, 'fecha_retiro': '2023-03-30', 'razon_retiro': 'Incapacidad', 'fecha_inicio': '2023-03-30'},
                         {'nombre': 'Angelica', 'apellido': 'Mora', 'edad': 42, 'talla': 1.90, 'peso': 75, 'brazo': 18, 'pecho': 95, 'cintura': 76, 'pierna': 40, 'fecha_retiro': '2023-03-30', 'razon_retiro': 'Incapacidad', 'fecha_inicio': '2023-03-30'},
                         {'nombre': 'Julian', 'apellido': 'Salazar', 'edad': 30, 'talla': 1.69, 'peso': 59, 'brazo': 17, 'pecho': 69, 'cintura': 60, 'pierna': 28, 'fecha_retiro': '2023-01-18', 'razon_retiro': 'Cambio de instructor', 'fecha_inicio': '2023-03-30'},
                         {'nombre': 'Bruno', 'apellido': 'Galan', 'edad': 26, 'talla': 1.53, 'peso': 60, 'brazo': 16, 'pecho': 72, 'cintura': 54, 'pierna': 20, 'fecha_retiro': '', 'razon_retiro': '', 'fecha_inicio': '2023-03-30'},
                        ]

        self.ejercicios = [
            {'nombre': 'Press de pierna', 'descripcion': 'Ejercicio de entrenamiento con pesas en el que el individuo empuja un peso o una resistencia con las piernas', 'youtube': 'https://www.youtube.com/watch?v=zac9BPZiUTQ', 'calorias': 120}, \
            {'nombre': 'Sentadilla', 'descripcion': 'Ejercicio de fuerza en el que se baja la cadera desde una posición de pie y luego vuelve a levantarse.', 'youtube': 'https://www.youtube.com/watch?v=l7aszLSPCVg', 'calorias': 80}, \
            {'nombre': 'Abducción de cadera', 'descripcion': 'Mover la pierna derecha hacia la derecha o alejarla del cuerpo y viceversa', 'youtube': 'https://www.youtube.com/watch?v=dILxTvY88uI', 'calorias': 90}
        ]

        self.entrenamientos = [{'persona': 'Federico', 'ejercicio': 'Press de pierna', 'fecha': '2023-01-18', 'repeticiones': 15, 'tiempo': 20},
                               {'persona': 'Federico', 'ejercicio': 'Sentadilla', 'fecha': '2023-01-18', 'repeticiones': 12, 'tiempo': 5},
                               {'persona': 'Federico', 'ejercicio': 'Press de pierna', 'fecha': '2023-03-11', 'repeticiones': 15, 'tiempo': 20},
                               {'persona': 'Bruno', 'ejercicio': 'Press de pierna', 'fecha': '2023-01-18', 'repeticiones': 15, 'tiempo': 30},
                               {'persona': 'Bruno', 'ejercicio': 'Sentadilla', 'fecha': '2023-07-02', 'repeticiones': 10, 'tiempo': 5}
                               ]

        self.reportes = [{'persona': 'Federico', 'imc': 21.4, 'clasificacion': 'Peso saludable', 'entrenamientos': [{'fecha': '2023-01-18', 'repeticiones': 27, 'calorias': 2760}, {'fecha': '2023-03-11', 'repeticiones': 15, 'calorias': 1800 }], 'total_repeticiones': 42, 'total_calorias': 4560},
                         {'persona': 'Bruno', 'imc': 25.6, 'clasificacion': 'Sobrepeso', 'entrenamientos': [{'fecha': '2023-01-18', 'repeticiones': 15, 'calorias': 1800}, {'fecha': '2023-07-02', 'repeticiones': 10, 'calorias': 800 }], 'total_repeticiones': 25, 'total_calorias': 2600}
                         ]


    def dar_personas(self):

        session = Session()

        try:
            personas = session.query(Persona).all()
            personas_dict = [
                {
                    'id': persona.id,
                    'nombre': persona.nombre,
                    'apellido': persona.apellido,
                    'edad':persona.edad,
                    'talla':persona.edad

                }
                for persona in personas
            ]
        except Exception as e:
            print(f"Ocurrió un error al consultar las personas: {e}")
            personas_dict = []
        finally:
            session.close()
        return personas_dict

    def crear_persona(self, nombre, apellido, edad, talla, peso, brazo, pecho, cintura, pierna):

        session = Session()
        fecha_inicio = datetime.now()

        new_persona = Persona(
            nombre=nombre,
            apellido=apellido,
            edad=edad,
            talla=talla,
            peso=peso,
            brazo=brazo,
            pecho=pecho,
            cintura=cintura,
            pierna=pierna,
            fecha_inicio=fecha_inicio,
        )

        session.add(new_persona)
        session.commit()
        session.close()
        print("Persona creada exitosamente.")

    def validar_crear_editar_persona(self, id_persona, nombre, apellido, edad, talla, peso, brazo, pecho, cintura, pierna):
        return ""
