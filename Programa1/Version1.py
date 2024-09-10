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

# Mostrar los resultados
print("\nSuma de las matrices:")
for fila in suma:
    print(fila)

print("\nResta de las matrices:")
for fila in resta:
    print(fila)
