from src.logica.FachadaEnForma import FachadaEnForma

class EntrenamientoEnForma(FachadaEnForma):

    def __init__(self):
        #Este constructor contiene los datos falsos para probar la interfaz
        self.personas = [{'nombre': 'Federico', 'apellido': 'Contreras', 'edad': 15, 'talla': 1.53, 'peso': 50, 'brazo': 15, 'pecho': 80, 'cintura': 70, 'pierna': 35, 'fecha_retiro': '', 'razon_retiro': ''},
                         {'nombre': 'Angelica', 'apellido': 'Mora', 'edad': 42, 'talla': 1.90, 'peso': 75, 'brazo': 18, 'pecho': 95, 'cintura': 76, 'pierna': 40, 'fecha_retiro': '2023-03-30', 'razon_retiro': 'Incapacidad'},
                         {'nombre': 'Julian', 'apellido': 'Salazar', 'edad': 30, 'talla': 1.69, 'peso': 59, 'brazo': 17, 'pecho': 69, 'cintura': 60, 'pierna': 28, 'fecha_retiro': '2023-01-18', 'razon_retiro': 'Cambio de instructor'},
                         {'nombre': 'Bruno', 'apellido': 'Galan', 'edad': 26, 'talla': 1.53, 'peso': 60, 'brazo': 16, 'pecho': 72, 'cintura': 54, 'pierna': 20, 'fecha_retiro': '', 'razon_retiro': ''},
                        ]

    def dar_personas(self):
        return self.personas.copy()

