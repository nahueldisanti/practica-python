""" 
    Introducción a la Programación 
    1er Cuatrimestre 2025
    Práctica 8: Pilas y Colas 
 """
from queue  import LifoQueue as Pila
from queue  import Queue as Cola
from random import randint

# Ejercicio 1.1
def generar_numeros_al_azar(cantidad: int, desde: int, hasta: int) -> Pila[int]:
    p: Pila[int] = Pila()
    for i in range(cantidad):
        n = randint(desde, hasta)
        p.put(n)

    print_pila(p)
    return p

# Ejercicio 1.3
def buscar_el_maximo(p: Pila[int]) -> int:
    # requiere: p no está vacía
    maximo: int = p.get() # Como p no vacía, tomamos el primer elemento y es el máximo hasta el momento
    p_aux: Pila[int] = Pila()
    p_aux.put(maximo)
    for i in range(p.qsize()):
        v = p.get()
        if v > maximo: 
            maximo = v
        else: 
            p_aux.put(v)

    return maximo

def buscar_el_maximo(p: Pila[int]) -> int:
    # requiere: p no está vacía
    maximo: int = p.get() # Como p no vacía, tomamos el primer elemento y es el máximo hasta el momento
    p_aux: Pila[int] = Pila()
    p_aux.put(maximo)
    while (not p.empty()):
        v = p.get()
        if v > maximo: 
            maximo = v
        else: 
            p_aux.put(v)

    return maximo

# Ejercicio 2.13.1
def armar_secuencia_de_bingo() -> Cola[int]:
    # requiere: True
    secuencia: list[int] = []
    
    for i in range(0,100):
        n = randint(0,99)
        secuencia.append(n)
    
    bolillero: Cola[int] = Cola(100)
    for i in range(bolillero.maxsize):
        bolillero.put(secuencia[i])
    # Estrategia posible: encolar cada elemento de "secuencia" en "bolillero" 
    print_cola(bolillero)
    return bolillero

# Ejercicio 2.13.2
def jugar_carton_de_bingo(carton: list[int], bolillero: Cola[int]) -> int:
    # requiere: carton contiene 12 números entre 0 y 99 inclusive, sin repetidos
    # requiere: bolillero contiene 100 números del 0 al 99 inclusive, sin repetidos
    aciertos: int = 0
    jugadas: int = 0
    bolillero_aux: Cola[int] = Cola()

    for i in range(bolillero: 


    # COMPLETAR
    # Estrategia posible: Mientras no acertemos todos los numeros del carton saco bolillas, actualizo la cantidad de aciertos y la cantidad de jugadas. Importante: Ir encolando los números que salen en bolillero_aux.
    
    # COMPLETAR
    # Estrategia posible: Terminar de vaciar el bolillero para poder reconstruirlo
        
    # COMPLETAR
    # Estrategia posible: Volver a meter los números de bolillas_aux en bolillero
    
    return jugadas

""" 
    FUNCIONES AUXILIARES
"""

def print_pila(p: Pila[int]) -> None:
    p_aux: Pila[int]= Pila()
    
    # Desapilo, imprimo y guardo en pila auxiliar
    while not p.empty():
        elem: int = p.get()
        p_aux.put(elem)
        print(elem, end="\n--\n")
 
    # Vuelvo a poner todo lo de pila auxiliar en p
    while not p_aux.empty():
        p.put(p_aux.get())

def print_cola(c: Cola[int]) -> None:
    c_aux: Cola[int]= Cola()
    
    # Desapilo, imprimo y guardo en pila auxiliar
    while not c.empty():
        elem: int = c.get()
        c_aux.put(elem)
        print(elem, end=" | ")
 
    # Vuelvo a poner todo lo de pila auxiliar en p
    while not c_aux.empty():
        c.put(c_aux.get())