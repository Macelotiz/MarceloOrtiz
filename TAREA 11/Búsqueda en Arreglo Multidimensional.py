# Programa 1: Búsqueda en Arreglo Multidimensional

# Definimos una matriz bidimensional de 3x3
matriz = [
    [5, 8, 12],
    [7, 3, 15],
    [9, 14, 6]
]

# Función para buscar un valor en la matriz
def buscar_valor(matriz, valor):
    for i in range(len(matriz)):  # Recorremos las filas
        for j in range(len(matriz[i])):  # Recorremos las columnas
            if matriz[i][j] == valor:
                return (i, j)  # Devolvemos la posición si se encuentra
    return None  # Si no se encuentra

# Programa principal
print("Matriz:")
for fila in matriz:
    print(fila)


# Definimos el valor a buscar (puedes cambiarlo o pedir al usuario con input)
valor_buscado = int(input("\nIngrese el valor que desea buscar en la matriz: "))

posicion = buscar_valor(matriz, valor_buscado)

if posicion:
    print(f" El valor {valor_buscado} se encuentra: fila {posicion[0]}, columna {posicion[1]}")
else:
    print(f" El valor {valor_buscado} no se encuentra en la matriz")
