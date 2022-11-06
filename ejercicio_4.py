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
        self.grado = -1

    def agregar_termino(self, termino, valor):
        aux = Nodo()
        dato= datoPolinomio(valor, termino)
        aux.info=dato
        if(termino > self.grado):
            aux.sig = self.termino_mayor
            self.termino_mayor = aux
            self.grado = termino
        else:
            actual = self.termino_mayor
            while(actual.sig is not None and termino < actual.sig.info.termino):
                actual = actual.sig
            aux.sig = actual.sig
            actual.sig = aux
    
    def eliminar_termino(self,termino):
        aux = self.termino_mayor
        if(self.grado == termino):
            self.termino_mayor=aux.sig
            del aux
        else:
            while(aux.sig is not None):
                if aux.sig.info.termino == termino:
                    aux.sig = aux.sig.sig
                    del aux.sig
                    return
                aux = aux.sig
    #Obtiene el valor de un monomio
    def obtener_valor(self, termino):
        aux = self.termino_mayor
        while(aux is not None and aux.info.termino > termino):
            aux = aux.sig
        if(aux is not None and aux.info.termino ==termino):
            return aux.info.valor
        else:
            return 0
    #Pinta un polinomio
    def imprime(self):
        actual = self.termino_mayor
        while(actual is not None):
            print("{}X{}".format(actual.info.valor, actual.info.termino))
            actual = actual.sig
    
    def restar(self, polinomio2):
        aux= Polinomio()
        mayor= self if(self.grado>polinomio2.grado)else polinomio2
        for i in range(0, mayor.grado+1):
            total = self.obtener_valor(i) - polinomio2.obtener_valor(i)
            if(total!=0):
                aux.agregar_termino(i, total)
        return aux
A = Polinomio()
A.agregar_termino(2,4)
A.agregar_termino(4,5)
A.imprime()
B = Polinomio()
B.agregar_termino(3,3)
B.imprime()
C = A.restar(B)
print("Completo")
C.imprime()
C.eliminar_termino(2)
print("Eliminado")
C.imprime()