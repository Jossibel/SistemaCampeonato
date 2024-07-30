from datetime import date
from torneo import Torneo
from equipo import Equipo
from entrenador import Entrenador
from partido import Partido
from campeonato import Campeonato
from models.tipo_campeonato import TipoCampeonato
from tabla_posiciones import TablaPosiciones

class Jugador:
    def __init__(self, nombre, numero):
        self.nombre = nombre
        self.numero = numero

MAX_JUGADORES = 11  # Limite máximo de jugadores por equipo

def ingresar_jugadores(numero_maximo):
    jugadores = []
    numeros_jugadores = set()  # Usamos un conjunto para verificar unicidad
    while len(jugadores) < numero_maximo:
        nombre_jugador = input("Ingrese el nombre del jugador (deje en blanco para terminar): ")
        if not nombre_jugador:
            if len(jugadores) >= 1:  # Asegura que al menos un jugador esté ingresado
                break
            else:
                print(f"Debe ingresar al menos un jugador. Quedan {numero_maximo - len(jugadores)} jugadores por ingresar.")
                continue
        while True:
            try:
                numero_jugador = int(input(f"Ingrese el número del jugador {nombre_jugador}: "))
                if numero_jugador in numeros_jugadores:
                    print("Número ya asignado. Por favor ingrese un número diferente.")
                else:
                    numeros_jugadores.add(numero_jugador)
                    jugadores.append(Jugador(nombre_jugador, numero_jugador))
                    break
            except ValueError:
                print("Número inválido. Por favor ingrese un número entero.")
    return jugadores

def main():
    print("Bienvenido al sistema de gestión de torneos de fútbol")

    # Ingresar datos para el entrenador (opcional)
    entrenador_nombre = input("Ingrese el nombre del entrenador (opcional): ")
    entrenador = Entrenador(nombre=entrenador_nombre) if entrenador_nombre else None

    # Ingresar datos para el equipo local
    equipo_local_nombre = input("Ingrese el nombre del equipo local: ")
    num_jugadores_local = int(input(f"Ingrese el número de jugadores para {equipo_local_nombre} (máx. {MAX_JUGADORES}): "))
    if num_jugadores_local > MAX_JUGADORES:
        print(f"El número máximo de jugadores por equipo es {MAX_JUGADORES}. Se ajustará al límite.")
        num_jugadores_local = MAX_JUGADORES
    equipo_local = Equipo(nombre=equipo_local_nombre, entrenador=entrenador)
    print(f"\nIngrese los jugadores del equipo local ({num_jugadores_local} jugadores):")
    equipo_local.jugadores = ingresar_jugadores(num_jugadores_local)

    # Ingresar datos para el equipo visitante
    equipo_visitante_nombre = input("Ingrese el nombre del equipo visitante: ")
    num_jugadores_visitante = int(input(f"Ingrese el número de jugadores para {equipo_visitante_nombre} (máx. {MAX_JUGADORES}): "))
    if num_jugadores_visitante > MAX_JUGADORES:
        print(f"El número máximo de jugadores por equipo es {MAX_JUGADORES}. Se ajustará al límite.")
        num_jugadores_visitante = MAX_JUGADORES
    equipo_visitante = Equipo(nombre=equipo_visitante_nombre, entrenador=entrenador)
    print(f"\nIngrese los jugadores del equipo visitante ({num_jugadores_visitante} jugadores):")
    equipo_visitante.jugadores = ingresar_jugadores(num_jugadores_visitante)

    # Ingresar los detalles del partido
    print("\nDetalles del partido:")
    while True:
        try:
            partido_fecha = input("Ingrese la fecha del partido (formato YYYY-MM-DD): ")
            partido_fecha = date.fromisoformat(partido_fecha)
            break
        except ValueError:
            print("Fecha inválida. Por favor ingrese la fecha en el formato YYYY-MM-DD.")

    partido = Partido(equipoLocal=equipo_local, equipoVisitante=equipo_visitante, fecha=partido_fecha)

    # Registrar resultado del partido
    while True:
        resultado = input("Ingrese el resultado del partido (ej. 2-2): ")
        if "-" in resultado and len(resultado.split("-")) == 2:
            try:
                goles_local, goles_visitante = map(int, resultado.split("-"))
                break
            except ValueError:
                print("Formato incorrecto. Asegúrese de ingresar números enteros para los goles.")
        else:
            print("Formato incorrecto. Use el formato 'X-X' para el resultado.")

    partido.registrarResultado(resultado)

    # Ingresar datos del campeonato
    campeonato_nombre = input("\nIngrese el nombre del campeonato: ")
    while True:
        try:
            campeonato_inicio = input("Ingrese la fecha de inicio del campeonato (formato YYYY-MM-DD): ")
            campeonato_inicio = date.fromisoformat(campeonato_inicio)
            break
        except ValueError:
            print("Fecha inválida. Por favor ingrese la fecha en el formato YYYY-MM-DD.")

    while True:
        try:
            campeonato_fin = input("Ingrese la fecha de fin del campeonato (formato YYYY-MM-DD): ")
            campeonato_fin = date.fromisoformat(campeonato_fin)
            break
        except ValueError:
            print("Fecha inválida. Por favor ingrese la fecha en el formato YYYY-MM-DD.")

    while True:
        try:
            tipo_campeonato = int(input("Ingrese el tipo de campeonato (1 para LIGA, 2 para COPA, 3 para TORNEO): "))
            if tipo_campeonato in [1, 2, 3]:
                break
            else:
                print("Tipo de campeonato inválido. Por favor ingrese 1, 2 o 3.")
        except ValueError:
            print("Tipo de campeonato inválido. Por favor ingrese un número entero.")

    campeonato = Campeonato(
        nombre=campeonato_nombre,
        fechaInicio=campeonato_inicio,
        fechaFin=campeonato_fin,
        tipo=TipoCampeonato(tipo_campeonato)
    )

    # Agregar equipos al campeonato
    campeonato.agregarEquipo(equipo_local)
    campeonato.agregarEquipo(equipo_visitante)

    # Crear y actualizar la tabla de posiciones
    tabla_posiciones = TablaPosiciones()
    if goles_local > goles_visitante:
        print(f"{equipo_local_nombre} gana el partido contra {equipo_visitante_nombre}")
        tabla_posiciones.actualizarTabla(equipo_local_nombre, 3, goles_local, goles_visitante)  # 3 puntos por ganar
        tabla_posiciones.actualizarTabla(equipo_visitante_nombre, 0, goles_visitante, goles_local)
    elif goles_local < goles_visitante:
        print(f"{equipo_visitante_nombre} gana el partido contra {equipo_local_nombre}")
        tabla_posiciones.actualizarTabla(equipo_visitante_nombre, 3, goles_visitante, goles_local)
        tabla_posiciones.actualizarTabla(equipo_local_nombre, 0, goles_local, goles_visitante)
    else:
        print(f"El partido entre {equipo_local_nombre} y {equipo_visitante_nombre} termina en empate")
        tabla_posiciones.actualizarTabla(equipo_local_nombre, 1, goles_local, goles_visitante)  # 1 punto por empatar
        tabla_posiciones.actualizarTabla(equipo_visitante_nombre, 1, goles_visitante, goles_local)

    # Mostrar resultados y tabla de posiciones
    print(f"\nResultado del partido: {partido.resultado}")
    print(f"Equipos en el campeonato '{campeonato.nombre}': {[equipo.nombre for equipo in campeonato.equipos]}")

    print("\nTabla de posiciones:")
    print("{:<3} {:<20} {:<3} {:<3} {:<3} {:<3} {:<3} {:<3} {:<3} {:<3}".format("Pos", "Equipo", "PJ", "PG", "PE", "PP", "GF", "GC", "GD", "PTS"))
    print("-" * 60)
    for pos, (equipo, data) in enumerate(tabla_posiciones.mostrarTabla(), start=1):
        print("{:<3} {:<20} {:<3} {:<3} {:<3} {:<3} {:<3} {:<3} {:<3} {:<3}".format(
            pos, equipo, data['PJ'], data['PG'], data['PE'], data['PP'], data['GF'], data['GC'], data['GD'], data['PTS']
        ))

if __name__ == "__main__":
    main()
