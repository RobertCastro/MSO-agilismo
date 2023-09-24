import sys
from src.vista.InterfazEnForma import App_EnForma
from src.logica.EntrenamientoEnForma import EntrenamientoEnForma
from src.Initialization import poblar_tabla_personas
from src.Initialization import poblar_tabla_ejercicio
from src.Initialization import poblar_tabla_entrenamiento

if __name__ == '__main__':
    # Punto inicial de la aplicación

    # poblar_tabla_personas()
    # poblar_tabla_ejercicio()
    # poblar_tabla_entrenamiento()
    logica = EntrenamientoEnForma()

    app = App_EnForma(sys.argv, logica)
    sys.exit(app.exec_())