
#Creación de una matriz como una lista de lista
def crear_matriz(numero_filas, numero_columnas):
    matriz = [None] * numero_filas
    for i in range(numero_filas):
        matriz[i] = [None] * numero_columnas
    return matriz

matriz = crear_matriz(3, 3)
print(matriz)


matriz_final = crear_matriz_final(3,3)
print(matriz_final)

def det(n):
    deter=1
    for x in range (n):
        deter=matriz[x][x]*deter
    print ('\nEl determinante de la matriz es = ', deter)







