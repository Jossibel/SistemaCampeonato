class Partido:
    def __init__(self, equipoLocal, equipoVisitante, fecha, resultado=None):
        self.equipoLocal = equipoLocal
        self.equipoVisitante = equipoVisitante
        self.fecha = fecha
        self.resultado = resultado

    def registrarResultado(self, resultado):
        self.resultado = resultado
