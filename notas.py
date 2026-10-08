def calcular_media(alumnos):
    """Calcula la nota media a partir de una lista de diccionarios de alumnos.

  Parámetros:
      alumnos (list of dict): Lista de diccionarios donde cada elemento
        representa
                              a un alumno e incluye obligatoriamente la clave
                              "nota" (int o float).

  Retorna:
      float: La nota media redondeada a dos decimales. Retorna 0 si la lista está vacía."""
    total = 0
    if len(alumnos) == 0:
        return 0
    for alumno in alumnos:
        total += alumno["nota"]
    return round(total/len(alumnos), 2)

alumnos = [
    {"nombre": "Ana", "nota": 8.5},
    {"nombre": "Luis", "nota": 4.0},
    {"nombre": "Marta", "nota": 7.0},
    {"nombre": "Pablo", "nota": 3.5},
    {"nombre": "Sara", "nota": 9.0},
]
aprobados = 0
suspendidos = 0
total = 0

for alumno in alumnos:
    total += alumno["nota"]
    if alumno["nota"] >= 5: 
        print(f"Nombre: {alumno["nombre"].upper()}, nota: {alumno["nota"]}. Está aprobado")
        aprobados += 1
    else:
        print(f"Nombre: {alumno["nombre"].upper()}, nota: {alumno["nota"]}. Está suspendido")
        suspendidos += 1


media = calcular_media(alumnos)

print(f"{len(alumnos)} alumnos, {aprobados} aprobados, {suspendidos} suspendidos, media {media}")