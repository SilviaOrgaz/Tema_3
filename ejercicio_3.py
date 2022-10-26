class Nave ():

    def __init__(self, nombre, largo, tripulacion, pasajeros):
        self.nombre = nombre
        self.largo = largo
        self.tripulacion = tripulacion
        self.pasajeros = pasajeros
    
    def __str__(self):
        return "{} de {} de largo con {} de tripulacion y con capacidad para {} pasajeros".format(self.nombre, self.largo, self.tripulacion, self.pasajeros)

def imprimir_lista(lista):
    for i in lista:
        print (i)

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


imprimir_lista(lista)