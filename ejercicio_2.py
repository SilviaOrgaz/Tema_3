
#Creación de una matriz como una lista de lista
def crear_matriz(numero_filas, numero_columnas):
    matriz = [None] * numero_filas
    for i in range(numero_filas):
        matriz[i] = [None] * numero_columnas
    return matriz

#Genero una matriz de grado dos de cuatro elementos
def insertar_elementos_grado_2(a, b, c , d):
    matriz = crear_matriz(2, 2)
    matriz[0][0] = a
    matriz[0][1] = b
    matriz[1][0] = c
    matriz[1][1] = d
    return matriz

#Calculo de un determinante de una matriz de grado 2
def determinante_grado_2(m2):
    return m2[0][0] * m2[1][1] - m2[0][1] * m2[1][0]


#Función iterativa
def determinante_grado_3(m3):
    A1 = m3[0][0] * determinante_grado_2(insertar_elementos_grado_2(m3[1][1], m3[1][2], m3[2][1], m3[2][2]))
    A2 = m3[0][1] * determinante_grado_2(insertar_elementos_grado_2(m3[1][0], m3[1][2], m3[2][0], m3[2][2]))
    A3 = m3[0][2] * determinante_grado_2(insertar_elementos_grado_2(m3[1][0], m3[1][1], m3[2][0], m3[2][1]))
    return A1 - A2 + A3

def determinante_grado_3_sarrus(m3):
    return m3[0][0]*m3[1][1]*m3[2][2] + m3[1][0] * m3[2][1] *m3[0][2] + m3[2][0] * m3[1][2] * m3[0][1] - m3[0][2] * m3[1][1] *[2][0] - m3[1][2] * m3[2][1] * m3[0][0]- m3[0][1]*m3[1][0]*m3[2][2]

matriz = [[1, 2, 4],[2, 3, 5],[8, 5, 9]]
print("El determinante iterativo es:",determinante_grado_3(matriz))
print("El determinante según Sarrus:",determinante_grado_3_sarrus(matriz))






