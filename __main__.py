import sys
from src.vista.InterfazEnForma import App_EnForma
from src.logica.EntrenamientoEnForma import EntrenamientoEnForma

if __name__ == '__main__':
    # Punto inicial de la aplicación

    logica = EntrenamientoEnForma()

    app = App_EnForma(sys.argv, logica)
    sys.exit(app.exec_())