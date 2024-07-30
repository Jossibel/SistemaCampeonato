# SistemaCampeonato
Arreglos del Diagrama 
Pruebas del Código 
![Captura de pantalla 2024-07-30 114208](https://github.com/user-attachments/assets/fc6e7e14-acd6-4f70-b7f9-a446ea6028d3)
![Captura de pantalla 2024-07-30 114323](https://github.com/user-attachments/assets/8cea45e1-980c-4210-9d2f-e34607d19014)
Estas clases y metodos se implemento del diagrama no se han implementado en el código:

Temporada

Atributos: año, torneos
Métodos: iniciarTemporada(), finalizarTemporada(), gestionarEstado()
Torneo

Atributos: nombre, fechaInicio, fechaFin
Métodos: agregarCampeonato(), eliminarCampeonato(), gestionarEstado(), finalizar(), iniciar()
SistemaCampeonato

Atributos: tipo, descripcion
Métodos: calcularGanador(), generarCalendario()
Competencia

Atributos: nombre, descripcion
Métodos: iniciar(), finalizar(), gestionarEstado()
Arbitro

Atributos: idArbitro, experiencia
Métodos: arbitrarPartido()
Inscripcion

Atributos: equipos, fecha
Métodos: aceptarInscripcion(), rechazarInscripcion()
Premio

Atributos: nombre, descripcion
Métodos: otorgar()
Estado

Atributos: nombre, ubicacion, capacidad
Métodos: reservarEstado(), liberarEstado(), verificarDisponibilidad()
Evento

Atributos: nombre, fecha, descripcion
Métodos: registrarEvento(), gestionar()
Resultado

Atributos: equipoLocal, equipoVisitante, golesLocal, golesVisitantes
Métodos: mostrarResultado()
Persona

Atributos: apellido, fechaNac, dni, sexo
Secretario

Atributos: idSecretario
Métodos: supervisar()
Supervisor

Atributos: idSupervisor
Directivo

Atributos: idDirectivo
Organizacion

Métodos: gestionar()
