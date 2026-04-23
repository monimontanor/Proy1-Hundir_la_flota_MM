# BATTLESHIP

import numpy as np

import random

from Utils_MM import crea_tablero, colocar_barcos, ask_coord, disparar, crear_barco


# PARTE 1: Creación de tableros (Función crear_tablero)
# _____________________________________________________________________________________#

tablero_jugador = crea_tablero()
tablero_rival = crea_tablero()
tablero_jug_pum = crea_tablero() #Para cuando dispare
tablero_riv_pum = crea_tablero() #Para cuando dispare
#print(tablero)


# Creación de listas para usar en colocar barcos

lista_barcos_jugador = [[(0,1),(1,1)], [(2,3), (2,4),(2,5)]]
lista_barcos_rival = [[(9,1),(9,2)], [(9,5),(9,6),(9,7), (9,8)]]

# PARTE 2: Colocación de los barcos en el tablero (Función colocar_barcos)

tablero_jugador = colocar_barcos(lista_barcos_jugador, tablero_jugador)
tablero_rival = colocar_barcos(lista_barcos_rival, tablero_rival)

#Vemos los tableros por pantalla

print("------------\n TABLERO JUGADOR \n---------------")
print(tablero_jugador)

print("------------\n TABLERO RIVAL \n -----------------")
print(tablero_rival)

# PARTE 3: Disparamos (Función disparar)

# Solicitar las coordenadas del dsiparo

print("--------------- \n VAMOS CON LAS COORDENADAS DONDE QUIERES DISPARAR \n-----------------")

f,c = ask_coord()

#Disparo al tablero rival

tablero_rival = disparar(f,c, tablero_rival)
print("--------------- \n ASÍ QUEDÓ TU EL TABLERO \n-----------------")

print(tablero_rival)

# PARTE 4: Creación del barco aleatorio

print("--------------- \n COORDENADAS DEL BARCO ALEATORIO \n-----------------")

#Se crea el barco y arroja sus coordenadas

barco = crear_barco(4)
print("Se ha generado el barco con las coordenadas: ", barco)





