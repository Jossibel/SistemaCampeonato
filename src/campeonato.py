class Campeonato:
    def __init__(self, nombre, fechaInicio, fechaFin, tipo):
        self.nombre = nombre
        self.fechaInicio = fechaInicio
        self.fechaFin = fechaFin
        self.tipo = tipo
        self.equipos = []

    def registrarCampeonato(self):
        pass

    def agregarEquipo(self, equipo):
        self.equipos.append(equipo)

    def gestionarEstado(self, estado):
        pass

    def generarCalendario(self):
        pass
