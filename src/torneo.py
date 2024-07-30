class Torneo:
    def __init__(self, nombre, fechaInicio, fechaFin):
        self.nombre = nombre
        self.fechaInicio = fechaInicio
        self.fechaFin = fechaFin
        self.campeonatos = []

    def agregarCampeonato(self, campeonato):
        self.campeonatos.append(campeonato)

    def eliminarCampeonato(self, campeonato):
        self.campeonatos.remove(campeonato)

    def gestionarEstado(self, estado):
        pass

    def iniciar(self):
        pass

    def finalizar(self):
        pass
