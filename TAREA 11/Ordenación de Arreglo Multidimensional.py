# Programa 2: Ordenación de Arreglo Multidimensional (con selección por input)

# Definimos una matriz bidimensional de 3x3
matriz = [
    [12, 5, 8],
    [7, 15, 3],
    [14, 9, 6]
]

# Función para ordenar una fila específica con Bubble Sort
def ordenar_fila(matriz, fila):
    # Copiamos la matriz original para no modificarla directamente
    matriz_ordenada = [fila.copy() for fila in matriz]

    # Obtenemos la fila que queremos ordenar
    fila_objetivo = matriz_ordenada[fila]

    # Algoritmo Bubble Sort
    n = len(fila_objetivo)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if fila_objetivo[j] > fila_objetivo[j + 1]:
                fila_objetivo[j], fila_objetivo[j + 1] = fila_objetivo[j + 1], fila_objetivo[j]

    matriz_ordenada[fila] = fila_objetivo
    return matriz_ordenada

# Mostramos la matriz original
print("Matriz original:")
for fila in matriz:
    print(fila)

# Pedimos al usuario que seleccione la fila a ordenar
while True:
    try:
        fila_a_ordenar = int(input("\nIngresa el número de la fila a ordenar (0, 1 o 2): "))
        if fila_a_ordenar in [0, 1, 2]:
            break
        else:
            print("Por favor ingresa un número válido (0, 1 o 2).")
    except ValueError:
        print("Debes ingresar un número.")

# Ordenamos la fila seleccionada
matriz_ordenada = ordenar_fila(matriz, fila_a_ordenar)

# Mostramos la matriz con la fila ordenada
print("\nMatriz con la fila ordenada:")
for fila in matriz_ordenada:
    print(fila)
