# BATTLESHIP

import numpy as np

from Utils_MM import crea_tablero, colocar_barcos, ask_coord, disparar


# ------ Creación de los Tableros; los inciiales y los de disparo -----------

tablero_jugador = crea_tablero()
tablero_rival = crea_tablero()
tablero_jug_pum = crea_tablero() #Para cuando dispare
tablero_riv_pum = crea_tablero() #Para cuando dispare
#print(tablero)


# --------Creación de listas para usar en colocar barcos------

lista_barcos_jugador = [[(0,1),(1,1)], [(2,3), (2,4),(2,5)]]
lista_barcos_rival = [[(9,1),(9,2)], [(9,5), (9,6),(9,7)]]

# ---- Defino los diferentes tableros--------------------------

tablero_jugador = colocar_barcos(lista_barcos_jugador, tablero_jugador)
tablero_rival = colocar_barcos(lista_barcos_rival, tablero_rival)

print("------------TABLERO JUGADOR---------------")
print(tablero_jugador)

print("------------TABLERO RIVAL-----------------")
print(tablero_rival)

# -------------- AHORA TOCA DISPARAR ----------------

# -------- Tengo que solicitar las coordenadas -------

print("--------------- VAMOS CON LAS COORDENADAS!-----------------")

f, c = ask_coord()
print(f,c)
 
#------- AHORA SI PUEDO DISPARAR ------------------

disparo_jugador = disparar(f,c, tablero_jugador)
print(disparo_jugador)