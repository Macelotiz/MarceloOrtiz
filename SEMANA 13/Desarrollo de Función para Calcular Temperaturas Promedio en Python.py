# Crear una matriz 3D para almacenar datos de temperaturas

# Ciudades, semanas y dias
ciudades = ["Machala", "Portoviejo", "Ambato"]
semanas = 4
dias = ["lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"]

def calcular_promedios(ciudades, temperaturas, dias):
    """
    Calcula el promedio de temperaturas por ciudad en un período de tiempo.

    Parámetros:
        ciudades (list): Lista con los nombres de las ciudades.
        temperaturas (list): Matriz 3D con temperaturas [ciudad][semana][día].
        dias (list): Lista de días de la semana.

    Retorna:
        dict: Diccionario con cada ciudad y su promedio general.
    """
    resultados = {}

    for i, ciudad in enumerate(ciudades):
        suma_total = 0
        conteo = 0
        for semana in temperaturas[i]:
            suma_total += sum(semana)
            conteo += len(dias)
        promedio = suma_total / conteo
        resultados[ciudad] = promedio

    return resultados

# Matriz 3D con valores de ejemplo
# temperaturas [ciudad][semana][dia]

temperaturas = [
    [   # Machala
        [ 77, 81, 80, 78, 84, 87, 91], # Semana 1
        [ 78, 79, 84, 85, 82, 87, 90], # Semana 2
        [ 79, 83, 81, 85, 84, 93, 94], # Semana 3
        [ 76, 77, 81, 78, 85, 88, 92]  # Semana 4
    ],
    [   # Portoviejo
        [ 75, 60, 69, 80, 70, 71, 78], # Semana 1
        [ 72, 65, 69, 78, 71, 76, 85], # Semana 2
        [ 82, 66, 67, 71, 77, 73, 85], # Semana 3
        [ 74, 87, 68, 73, 75, 71, 84]  # Semana 4
    ],
    [   # Ambato
        [ 90, 82, 95, 92, 89, 86, 83], # Semana 1
        [ 81, 92, 95, 91, 88, 85, 84], # Semana 2
        [ 91, 93, 95, 92, 89, 86, 83], # Semana 3
        [ 82, 92, 94, 81, 85, 91, 80]  # Semana 4
    ]
]

# Calcular el promedios semanales por ciudad
for i, ciudad in enumerate(ciudades):
    print(f"\nciudad: {ciudad}")
    for semana in range(semanas):
        suma= 0
        for dia in range(len(dias)):
            suma += temperaturas[i][semana][dia]
        promedio = suma / len(dias)
        print(f" Semana {semana +1}: Promedio = {promedio:.2f} ºC")

# Llamada a la función
promedios = calcular_promedios(ciudades, temperaturas, dias)
print()
# Mostrar resultados
print("Promedio general de temperaturas por ciudad:")
for ciudad, promedio in promedios.items():
    print(f" {ciudad}: {promedio:.2f} ºC")