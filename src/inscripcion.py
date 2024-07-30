class Inscripcion:
    def __init__(self):
        self.equipos = []

    def aceptarInscripcion(self, equipo):
        self.equipos.append(equipo)

    def rechazarInscripcion(self, equipo):
        self.equipos.remove(equipo)
