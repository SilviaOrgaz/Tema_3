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
        print i

lista = []
A = Nave("Halcón Milenario", 100, 3, 5)
lista.append(A)
B = Nave("Estrella de la Muerte", 10000, 100, 2000)
lista.append(B)
imprimir_lista(lista)