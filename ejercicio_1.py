#Para realizar de forma recursiva este ejercicio hay que hacer dos por el anterior más uno.
def hanoi(n):
    if n == 1:
        contador = 1
    else:
        contador = (2* hanoi(n-1)+1)
    return contador

n = int(input("Introduce el número de discos de la Torre Hanói: "))
print("Se necesitan {} movimientos para mover {} discos".format(hanoi(n), n))

