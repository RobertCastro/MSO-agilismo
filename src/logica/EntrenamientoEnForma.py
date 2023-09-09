from src.logica.FachadaEnForma import FachadaEnForma

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

