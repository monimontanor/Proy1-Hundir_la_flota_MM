#FUNCIONES DEL JUEGO BATTLESHIP

import numpy as np
import random

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

# FUNCIÓN DISPARAR

    #Solicitar las coordenadas

def ask_coord():
    
    fila = int(input("Introduce la coordenada de la fila (OJO: entre el 0 y el 9): ")) #Para convertirla en int
    columna = int(input("Introduce la coordenada de la columna (OJO: entre el 0 y el 9): ")) #Para convertirla en int
    return fila, columna

    #Disparar 

def disparar (fila, columna, tablero):
    
    if tablero[fila][columna] == "O":
            tablero[fila][columna] = "X"
            print("Te han tocadooooo!")
    elif tablero[fila][columna] == "-":
            tablero[fila][columna] = "A"
            print("Aguaaaaaa!")
    else:
            print("Ahí ya disparaste") #Para evitar disparos repetidos cuando vuelva el turno
    return tablero

#FUNCIÓN CREAR BARCO ALEATORIO

def crear_barco(eslora):
    
    # 1. Elegimos orientación aleatoria (0 o 1)
    opcion = random.randint(0, 1)
    
    if opcion == 0:
        orientacion = "horizontal"
    else:
        orientacion = "vertical"
    
    # 2. Creamos el barco según orientación
    
    if orientacion == "horizontal":
        
        # fila fija
        fila = random.randint(0, 9)
        
        # columna ajustada para que no se salga
        columna = random.randint(0, 10 - eslora)
        
        # generamos casillas
        barco = [(fila, columna + i) for i in range(eslora)]
    
    else:
        
        # columna fija
        columna = random.randint(0, 9)
        
        # fila ajustada para que no se salga
        fila = random.randint(0, 10 - eslora)
        
        # generamos casillas
        barco = [(fila + i, columna) for i in range(eslora)]
    
    return barco






