class Nave ():

    def __init__(self, nombre, largo, tripulacion, pasajeros):
        self.nombre = nombre
        self.largo = largo
        self.tripulacion = tripulacion
        self.pasajeros = pasajeros
    
    def __str__(self):
        return "{}: {}, {}, {}".format(self.nombre, self.largo, self.tripulacion, self.pasajeros)

#Imprime la lista con las naves
def imprimir_lista(lista):
    print("Nombre, largo, tripulación, pasajeros")
    for i in lista:
        print (i)

#Impreme la nave y sus características
def imprimir(lista, nombre):
    for i in lista:
        if i.nombre == nombre:
            print (i)

#Imprime los primeros cinco elementos
def imprimir_n_elemntos(lista, longitud):
    for i in range(longitud):
        print(lista[i])

#Imprime las naves con n o más pasajeros
def imprimir_n_pasajeros(lista, n):
    for i in lista:
        if i.pasajeros >= n:
            print (i)

#Naves que comiencen por n
def imprimir_n_naves(lista, n):
    contador = 0
    for i in lista:
        if i.nombre[0] == n[0] and i.nombre[1] == n[1]:
            print(i)
            contador+=1
    if contador == 0:
        print("Ninguna nave empieza por esas letras")
            

lista = []
A = Nave("Halcón Milenario", 100, 3, 5)
lista.append(A)
B = Nave("Estrella de la Muerte", 10000, 100, 2000)
lista.append(B)
C = Nave("La Pinta", 500, 5, 10)
lista.append(C)
D = Nave("La Niña", 2000, 300, 8)
lista.append(D)
E = Nave("La Santa María", 1000, 7, 15)
lista.append(E)
G = Nave("Depredador", 200, 4, 6)
lista.append(G)
H = Nave("Veloz", 10, 1, 2)
lista.append(H)

#Listado ordenado por nombre de las naves de manera ascendente
lista_nombre = sorted(lista, key = lambda x:x.nombre)
imprimir_lista(lista_nombre)

#Listado ordenado por largo de las naves de manera descendente
lista_largo = sorted(lista, key = lambda x:x.largo, reverse = True)
imprimir_lista(lista_largo)

#Muestra toda la información del Halcón Milenario y de la Estrella de la Muerte
imprimir(lista, "Halcón Milenario")
imprimir(lista, "Estrella de la Muerte")

#Las cinco naves con mayor cantidad de pasajeros
lista_pasajeros = sorted(lista, key = lambda x:x.pasajeros, reverse = True)
imprimir_n_elemntos(lista_pasajeros, 5)

#Nave que requiere mayor cantidad de tripulación
lista_tripulacion = sorted(lista, key = lambda x:x.tripulacion, reverse = True)
imprimir_n_elemntos(lista_tripulacion, 1)

#Naves que puede llevar 6 o más pasajeros
imprimir_n_pasajeros(lista, 6)

#Nave más pequeña y más grandes
print(lista_largo[0])
print(lista_largo[-1])

#Naves que comienzan por AT
imprimir_n_naves(lista, "AT")