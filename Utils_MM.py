#FUNCIONES DEL JUEGO BATTLESHIP

import numpy as np

#FUNCIÓN DE CREAR TABLERO

def crea_tablero (): #No recibe nada
    tablero = np.full ((10,10), "-")
    return tablero

#Colocar los barcos manualmente 

def colocar_barcos (lista_barcos, tablero):
    for i in lista_barcos:
        for j in i:
            tablero [j] = "O"
    return tablero

# CREAR LOS BARCOS

    #Solicitar las coordenadas

def ask_coord():
    fila = input("Introduce la coordenada de la fila (OJO: entre el 0 y el 9): ")
    columna = input("Introduce la coordenada de la columna (OJO: entre el 0 y el 9): ")    
    return fila, columna

def disparar (fila, columna, tablero):
    
          
    if tablero[fila][columna] == "O":
        tablero[fila][columna] = "X"
        print("Te han tocado")
    elif tablero[fila][columna] == "#":
        tablero[fila][columna] = "A"
        print("Agua!")
    else:
        print("Ahí ya disparaste")
    
    return tablero
