#He creado este ejercicio en el repositrio de ejercicio_coches
class Nodo(object):
    info, sig = None, None

class datoPolinomio(object):

    def __init__(self, valor, termino):
        self.valor = valor
        self.termino = termino

class Polinomio(object):

    def __init__(self):
        self.termino_mayor = None
        self.ggrado = -1

    def agregar_termino(self, termino, valor):