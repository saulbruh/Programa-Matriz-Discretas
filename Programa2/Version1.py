# Definimos las dos matrices
matriz1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matriz2 = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]

# Función para sumar dos matrices
def sumar_matrices(matriz1, matriz2):
    resultado = []
    for i in range(len(matriz1)):
        fila = []
        for j in range(len(matriz1[0])):
            fila.append(matriz1[i][j] + matriz2[i][j])
        resultado.append(fila)
    return resultado

# Función para restar dos matrices
def restar_matrices(matriz1, matriz2):
    resultado = []
    for i in range(len(matriz1)):
        fila = []
        for j in range(len(matriz1[0])):
            fila.append(matriz1[i][j] - matriz2[i][j])
        resultado.append(fila)
    return resultado

# Función para multiplicar una matriz por un escalar
def multiplicar_por_escalar(matriz, escalar):
    resultado = []
    for i in range(len(matriz)):
        fila = []
        for j in range(len(matriz[0])):
            fila.append(matriz[i][j] * escalar)
        resultado.append(fila)
    return resultado

# Mostrar las matrices originales
print("Matriz 1:")
for fila in matriz1:
    print(fila)

print("\nMatriz 2:")
for fila in matriz2:
    print(fila)

# Sumar y restar las matrices
suma = sumar_matrices(matriz1, matriz2)
resta = restar_matrices(matriz1, matriz2)

# Mostrar los resultados de la suma y resta
print("\nSuma de las matrices:")
for fila in suma:
    print(fila)

print("\nResta de las matrices:")
for fila in resta:
    print(fila)

# Multiplicar los resultados por 2
suma_por_2 = multiplicar_por_escalar(suma, 2)
resta_por_2 = multiplicar_por_escalar(resta, 2)

# Mostrar los resultados de la multiplicación por 2
print("\nSuma de las matrices multiplicada por 2:")
for fila in suma_por_2:
    print(fila)

print("\nResta de las matrices multiplicada por 2:")
for fila in resta_por_2:
    print(fila)
