
#Creación de una matriz como una lista de lista
def crear_matriz(numero_filas, numero_columnas):
    matriz = [None] * numero_filas
    for i in range(numero_filas):
        matriz[i] = [None] * numero_columnas
    return matriz


#Calculo de un determinante de una matriz de grado 2
def determinante_grado_2(m2):
    return m2[0][0] * m2[1][1] - m2[0][1] * m2[1][0]

#Genero una matriz de grado dos de cuatro elementos
def insertar_elementos_grado_2(a, b, c , d):
    matriz = crear_matriz(2, 2)
    matriz[0][0] = a
    matriz[0][1] = b
    matriz[1][0] = c
    matriz[1][1] = d
    return matriz

def determinante_grado_3(m3):
    A1 = m3[0][0] * determinante_grado_2(insertar_elementos_grado_2(m3[1][1], m3[1][2], m3[2][1], m3[2][2]))
    A2 = m3[0][1] * determinante_grado_2(insertar_elementos_grado_2(m3[1][1], m3[1][2], m3[2][1], m3[2][2]))
    deter=1
    for x in range (n):
        deter=matriz[x][x]*deter
    print ('\nEl determinante de la matriz es = ', deter)




matriz = crear_matriz(2, 3)
print(matriz)





