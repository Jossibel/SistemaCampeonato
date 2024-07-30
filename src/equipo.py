class Equipo:
    def __init__(self, nombre: str, entrenador):
        self.nombre = nombre
        self.jugadores = []
        self.entrenador = entrenador

    def agregarJugador(self, jugador):
        self.jugadores.append(jugador)

    def eliminarJugador(self, jugador):
        self.jugadores.remove(jugador)

    def listarJugadores(self):
        return self.jugadores
