from datetime import date

class Persona:
    def __init__(self, apellido: str, cedula: str, fechaNacimiento: date, nacionalidad: str, sexo: str):
        self.apellido = apellido
        self.cedula = cedula
        self.fechaNacimiento = fechaNacimiento
        self.nacionalidad = nacionalidad
        self.sexo = sexo
