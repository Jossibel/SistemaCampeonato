from datetime import date
class Evento:
    def __init__(self, nombre: str, fecha: date, descripcion: str):
        self.nombre = nombre
        self.fecha = fecha
        self.descripcion = descripcion

    def registrarEvento(self):
        pass

    def gestionar(self):
        pass
