from collections import defaultdict
from src.logica.FachadaEnForma import FachadaEnForma
from src.modelo.declarative_base import Session
from src.modelo.Persona import Persona
from src.modelo.Ejercicio import Ejercicio
from src.modelo.Entrenamiento import Entrenamiento
from datetime import date, time
import validators
from datetime import datetime
import re

class EntrenamientoEnForma(FachadaEnForma):

    def dar_personas(self):
        session = Session()
        personas = session.query(Persona).order_by(Persona.nombre.asc(), Persona.apellido.asc()).all()
            
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
    
    
    def dar_ejercicios(self):

        session = Session()
        ejercicios = session.query(Ejercicio).order_by(Ejercicio.nombre.asc()).all()

        if len(ejercicios) > 0:
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
            return ejercicios_dict
        
        else:
            return []

    
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

    def validar_crear_editar_ejercicio(self, nombre, descripcion, enlace, calorias):
        session = Session()

        if not nombre or not descripcion or not enlace or not calorias:
            return "Complete todos los campos"
        if len(nombre) > 200:   
            return "La extensión max de caracteres del nombre debe ser 200"
        if not re.match('^[a-zA-Z0-9 ]*$', nombre):
            return "El nombre solo debe contener caracteres alfanuméricos y espacios"
        if len(descripcion) > 200:   
            return "La extensión max de caracteres de la descripcion debe ser 200"
        if not validators.url(enlace):
            return "El enlace no es una URL válida"
        
        ejercicio_existente = session.query(Ejercicio).filter(Ejercicio.nombre == nombre).first()
        if ejercicio_existente:
            session.close()
            return "Ya existe un ejercicio con este nombre"


        return ""
    
    def dar_entrenamientos(self, id_persona):
        print(id_persona)
        
        session = Session()

        persona = session.query(Persona).filter(Persona.id == id_persona).first()
        entrenamientos = session.query(Entrenamiento).filter(Entrenamiento.persona_id == id_persona).all()
        entrenamientos.sort(key=lambda x: datetime.strptime(x.fecha, '%Y-%m-%d'), reverse=True)

        return  [
            {
                'persona': persona.nombre,
                'ejercicio': entrenamiento.ejercicio.nombre,
                'fecha': entrenamiento.fecha,
                'repeticiones': entrenamiento.repeticiones,
                'tiempo': entrenamiento.tiempo
            }
            for entrenamiento in entrenamientos
        ]

    def validar_crear_editar_entrenamiento(self, persona, ejercicio, fecha, repeticiones, tiempo):
        tiempo_pattern = re.compile(r'^([0-1]?[0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]$')
        fecha_pattern = r'^\d{4}-\d{2}-\d{2}$'
        if repeticiones != "":
            repeticiones = int(repeticiones)
        
        if not ejercicio:
            return "Complete todos los campos"
        if not fecha:
            return "El campo fecha está vacío"
        if not repeticiones:
            return "El campo repeticiones está vacío"
        if not tiempo:
            return "El campo tiempo está vacío"
        if not isinstance(repeticiones, int) or repeticiones <= 0:
            return "Las repeticiones deben ser un número entero positivo"
        if not tiempo_pattern.match(str(tiempo)):
            return "El tiempo no tiene el formato correcto (hh:mm:ss)"
        if not re.fullmatch(fecha_pattern, str(fecha)):
            return "La fecha no tiene el formato correcto (aaaa-mm-dd)"
            
        return ""
    
    def crear_entrenamiento(self, persona, ejercicio, fecha, repeticiones, tiempo):

        session = Session()
        ejercicio = session.query(Ejercicio).filter_by(nombre=ejercicio).first() 
        persona_id = persona['id']
        ejercicio_id = ejercicio.id

        nuevo_entrenamiento = Entrenamiento(

            fecha = fecha,
            repeticiones = int(repeticiones), 
            tiempo = tiempo,
            persona_id = persona_id, 
            ejercicio_id = ejercicio_id
        )

        session.add(nuevo_entrenamiento)
        session.commit()
        session.close()
        return nuevo_entrenamiento

    def dar_persona(self, id_persona):
        session = Session()
        single_persona = session.query(Persona).filter(Persona.id == id_persona).first()
        session.close()
        
        if single_persona:
            persona = {
                "id": single_persona.id,
                "nombre": single_persona.nombre,
                "apellido": single_persona.apellido,
                'edad': single_persona.edad,
                'talla': single_persona.talla,
                'peso': single_persona.peso,
                'brazo': single_persona.brazo,
                'pecho': single_persona.pecho,
                'cintura': single_persona.cintura,
                'pierna': single_persona.pierna,
                'fecha_inicio': single_persona.fecha_inicio,
                'fecha_retiro': single_persona.fecha_retiro,
                'razon_retiro': single_persona.razon_retiro,
                'estado': single_persona.estado
            }
            return persona
        else:
            return None

    def dar_reporte(self, id_persona):
        session = Session()
        persona = session.query(Persona).filter_by(id=id_persona).first()

        imc = self.calcularIMC(persona)  # Todo: Implementar esta función
        clasificacionImc = self.clasificarIMC(imc)  # Todo: Implementar esta función

        resultadoFecha = self.agruparDatosEntrenamiento(persona.Entrenamiento)

        totalCalorias = sum(e['calorias'] for e in resultadoFecha)
        totalRepeticiones = sum(e['repeticiones'] for e in resultadoFecha)

        return {
            'persona': vars(persona),
            'estadisticas': {
                'imc': imc,
                'clasificacion': clasificacionImc,
                'entrenamientos': resultadoFecha,
                'total_repeticiones': totalRepeticiones,
                'total_calorias': totalCalorias
            }
        }

    def calcularIMC(self, persona):
        return ''

    def clasificarIMC(self, imc):
        return ''

    def agruparDatosEntrenamiento(self, entrenamientos):
        resultadosAgrupados = defaultdict(list)
        resultadoFecha = []

        for entrenamiento in entrenamientos:
            fecha = entrenamiento.fecha
            consumoCalorico = round(float(entrenamiento.repeticiones) * float(entrenamiento.ejercicio.calorias), 2)
            resultadosAgrupados[fecha].append({
                'consumo_calorico': consumoCalorico,
                'repeticiones': entrenamiento.repeticiones
            })

        for fecha, resultadosItem in resultadosAgrupados.items():
            totalConsumoCalorico = sum(resultado['consumo_calorico'] for resultado in resultadosItem)
            cantidadRepeticiones = sum(resultado['repeticiones'] for resultado in resultadosItem)

            resultadoFecha.append({
                'fecha': fecha,
                'calorias': round(totalConsumoCalorico, 2),
                'repeticiones': cantidadRepeticiones
            })

        return resultadoFecha

    def editar_ejercicio(self, id_ejercicio, nombre, descripcion, enlace, calorias):
        
        return "editar_ejercicio"
       
