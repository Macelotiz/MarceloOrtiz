# Crear una matriz 3D para almacenar datos de temperaturas
# Primera dimensión: Ciudades (3 ciudades)
# Segunda dimensión: Semanas (4 semanas)
# Tercera dimensión: Días de la semana (7 días)
temperaturas = [
    [   # Ciudad Machala
        [ 77, 81, 80, 78, 84, 87, 91], # Semana 1
        [ 78, 79, 84, 85, 82, 87, 90], # Semana 2
        [ 79, 83, 81, 85, 84, 93, 94], # Semana 3
        [ 76, 77, 81, 78, 85, 88, 92]  # Semana 4
    ],
    [   # Ciudad Portoviejo
        [ 75, 60, 69, 80, 70, 71, 78], # Semana 1
        [ 72, 65, 69, 78, 71, 76, 85], # Semana 2
        [ 82, 66, 67, 71, 77, 73, 85], # Semana 3
        [ 74, 87, 68, 73, 75, 71, 84]  # Semana 4
    ],
    [   # Ciudad Ambato
        [ 90, 82, 95, 92, 89, 86, 83], # Semana 1
        [ 81, 92, 95, 91, 88, 85, 84], # Semana 2
        [ 91, 93, 95, 92, 89, 86, 83], # Semana 3
        [ 82, 92, 94, 81, 85, 91, 80]  # Semana 4
    ]
]

# Calcular el promedio de temperaturas para cada ciudad y semana
for i, ciudad in enumerate(ciudades):
    print(f"\nCiudad: {ciudad}")
    for semana_in range(semanas):
        suma= 0
        for dia in range(len(dias)):
            suma += temperaturas[i][semana][dia]
        promedio = suma / len(dias)
        print(f" Semana {semana +1}: Promedio = {promedio: .2f} ºC")


