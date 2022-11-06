
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

#He creado el determinante de una matriz por el método de Sarrus
def determinante_grado_3_sarrus(m3):
    A1 = m3[0][0]*m3[1][1]*m3[2][2] + m3[1][0] * m3[2][1] *m3[0][2] + m3[2][0] * m3[1][2] * m3[0][1]
    A2 = m3[0][2] * m3[1][1] * m3[2][0] + m3[1][2] * m3[2][1] * m3[0][0] + m3[0][1] * m3[1][0] * m3[2][2]
    return A1 - A2

#He printado la matriz
def dibujar_matriz(m3):
    print("La matriz es:")
    for i in range(len(m3)):
        print(m3[i])


#matriz = [[1, 2, 4],[2, 3, 5],[8, 5, 9]]
#dibujar_matriz(matriz)
#print("El determinante iterativo es:",determinante_grado_3(matriz))
#print("El determinante según Sarrus:",determinante_grado_3_sarrus(matriz))

#Otra forma para hacer el ejercicio
def crear_matriz_segunda(numero_filas, numero_columnas):
    matriz = [None] * numero_filas
    for i in range (numero_filas):
        matriz[i]= [None] * numero_columnas
    return matriz

def dibujar_matriz_segunda(matriz):
    print("La matriz es: ")
    for i in range(len(matriz)):
        print (matriz[i])

#Función que recibe una matriz  una posición y elimina la columna de esa posición y los de la primera fila.
def crear_adjuntos(matriz, columna_eliminar):
    rango = len(matriz) 
    matriz_final=crear_matriz_segunda(rango-1, rango-1)
    for i in range(1, rango):
        aux = 0
        for j in range(rango):
            if j != columna_eliminar:
                matriz_final[i-1][aux] = matriz[i][j]
                aux+=1
    return matriz_final

def calcula_determinante(matriz):
    if len(matriz) == 2:
        return matriz[0][0] * matriz[1][1] - matriz[0][1] * matriz[1][0]
    acumulable = 0
    for i in range (len(matriz)):
        determinante = matriz[0][i] * calcula_determinante(crear_adjuntos(matriz, i))
        print(determinante)
        acumulable +=determinante
    return acumulable
    
matriz = [[1, 2, 4],[2, 3, 5],[8, 5, 9]]
dibujar_matriz(matriz)
adjunto = crear_adjuntos(matriz,2)
dibujar_matriz(adjunto)
determinante = calcula_determinante(matriz)
print(determinante)





