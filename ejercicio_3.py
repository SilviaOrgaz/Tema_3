class Nave ():

    def __init__(self, nombre, largo, tripulacion, pasajeros):
        self.nombre = nombre
        self.largo = largo
        self.tripulacion = tripulacion
        self.pasajeros = pasajeros
    
    def __str__(self):
        return "{}: {}, {}, {}".format(self.nombre, self.largo, self.tripulacion, self.pasajeros)

def buscar(nombre, lista):
    for i in lista:
        if nombre == "":
            print (i)

def imprimir_lista(lista):
    print("Nombre, largo, tripulación, pasajeros")
    for i in lista:
        print (i)

Nave = Nave()
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
#imprimir_lista(lista_nombre)

#Listado ordenado por largo de las naves de manera descendente
lista_largo = sorted(lista, key = lambda x:x.largo, reverse = True)
#imprimir_lista(lista_largo)

#Muestra toda la información del Halcón Milenario y de la Estrella de la Muerte
Nave.buscar(lista)
