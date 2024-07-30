class TablaPosiciones:
    def __init__(self):
        self.tabla = {}

    def actualizarTabla(self, equipo, puntos, goles_a_favor, goles_en_contra):
        if equipo not in self.tabla:
            self.tabla[equipo] = {
                'PJ': 0,  # Partidos Jugados
                'PG': 0,  # Partidos Ganados
                'PE': 0,  # Partidos Empatados
                'PP': 0,  # Partidos Perdidos
                'GF': 0,  # Goles a Favor
                'GC': 0,  # Goles en Contra
                'GD': 0,  # Diferencia de Goles
                'PTS': 0  # Puntos
            }
        equipo_info = self.tabla[equipo]
        equipo_info['PJ'] += 1
        equipo_info['GF'] += goles_a_favor
        equipo_info['GC'] += goles_en_contra
        equipo_info['GD'] = equipo_info['GF'] - equipo_info['GC']
        equipo_info['PTS'] += puntos

        if puntos == 3:
            equipo_info['PG'] += 1
        elif puntos == 1:
            equipo_info['PE'] += 1
        else:
            equipo_info['PP'] += 1

    def mostrarTabla(self):
        return sorted(self.tabla.items(), key=lambda x: (-x[1]['PTS'], -x[1]['GD'], -x[1]['GF']))

