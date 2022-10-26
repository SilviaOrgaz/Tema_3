def hanoi(n):
    if n == 1:
        contador = 1
    else:
        contador = (2* hanoi(n-1)+1)
    return contador