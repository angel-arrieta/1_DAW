import random

def imprimir_tablero():
    columnas = "ABCDEFGHIJ"
    print(" ", end="")
    for letra in columnas:
        print(letra, end=" ")
    # for i in range(10):
    #   print(chr(65+i), end=" ")
    print()
    for orden, fila in enumerate(tablero()):
        # print(orden+1, end=" "+(" " if orden+1<10 else ""))
        print(orden+1, end=" ")
        if orden+1 < 10:
            print(" ", end="")
        for celda in fila:
            print(celda, end=" ")
        print()

# Crea tablero 10x10
# versión con listas por comprensión


def tablero(filas=10, columnas=10):
    return [[" " for _ in range(columnas)] for _ in range(filas)]


imprimir_tablero()

# versión loser


"""""
if __name__ == "__main__":
    tablero = []
    for _ in range(10):
        fila = []
        for _ in range(10):
            fila.append("V")
        tablero.append(fila)
"""
