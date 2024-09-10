# Función para crear una matriz a partir de la entrada del usuario
def crear_matriz(filas, columnas):
    matriz = []
    for i in range(filas):
        fila = []
        for j in range(columnas):
            valor = int(input(f"Ingrese el valor de la posición [{i+1}, {j+1}]: "))
            fila.append(valor)
        matriz.append(fila)
    return matriz

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

# Pedir al usuario el tamaño de las matrices
filas = int(input("Ingrese el número de filas para las matrices: "))
columnas = int(input("Ingrese el número de columnas para las matrices: "))

# Crear las dos matrices con los valores ingresados por el usuario
print("\nIngrese los valores para la Matriz 1:")
matriz1 = crear_matriz(filas, columnas)

print("\nIngrese los valores para la Matriz 2:")
matriz2 = crear_matriz(filas, columnas)

# Pedir al usuario el escalar para multiplicar las matrices
escalar = int(input("\nIngrese el valor del escalar por el cual desea multiplicar las matrices: "))

# Mostrar las matrices originales
print("\nMatriz 1:")
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

# Multiplicar los resultados por el escalar ingresado
suma_por_escalar = multiplicar_por_escalar(suma, escalar)
resta_por_escalar = multiplicar_por_escalar(resta, escalar)

# Mostrar los resultados de la multiplicación por el escalar
print(f"\nSuma de las matrices multiplicada por {escalar}:")
for fila in suma_por_escalar:
    print(fila)

print(f"\nResta de las matrices multiplicada por {escalar}:")
for fila in resta_por_escalar:
    print(fila)
