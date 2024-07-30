class Jugador:
    def __init__(self, nombre, posicion):
        self.nombre = nombre
        self.posicion = posicion
        self.estadisticas = Estadisticas()

    def actualizarEstadisticas(self, tipo, valor):
        self.estadisticas.actualizarEstadisticas(tipo, valor)
