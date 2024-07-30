class Estadisticas:
    def __init__(self):
        self.goles = 0
        self.asistencias = 0
        self.partidosJugados = 0

    def actualizarEstadisticas(self, tipo, valor):
        if tipo == "goles":
            self.goles += valor
        elif tipo == "asistencias":
            self.asistencias += valor
        elif tipo == "partidosJugados":
            self.partidosJugados += valor
