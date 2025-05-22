""" 
    Introducción a la Programación 
    1er Cuatrimestre 2025
    Práctica 7: Funciones sobre listas
"""


https://bit.ly/ip1c2025-guia8

m = [[1,2,3,4], [2,3,4,5], [4,5,6,7], [5,4,1,2]]

def ordenados(s: list[int]) -> bool :
    i: int = 1
    while 0 < i and i < len(s):
        if s[i] < s[i-1]: 
            return False
        i = i + 1
    return True

# Función opcional
def columnas(m: list[list[int]]) -> list[list[int]]:
    columnas: list[list[int]] = []
    for i in range(len(m[i])):
        for j in range(len(m)):
            columnas[i][j].append(m[j][i])
    return columnas

def columnas_ordenadas(m: list[list[int]]) -> list[bool]:
    columnas_ordenadas: [list[bool]] = [] 
    for i in range(len(m)):
        columnas_ordenadas.append(ordenados(m[i]))
    return columnas_ordenadas

# Procedimiento auxiliar
def print_matriz(m: list[list[int]]) -> None:
    for f in m:
        print(f)