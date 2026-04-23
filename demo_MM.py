
from Utils_MM import crea_tablero, crear_barco, colocar_barco, ask_coord, disparar


# 1. CREAR TABLERO
tablero = crea_tablero()

print("\n🔹 TABLERO INICIAL")
print(tablero)


# 2. CREAR BARCO (solo generación)
barco = crear_barco(3)

print("\n🔹 BARCO GENERADO:")
print(barco)


# 3. COLOCAR BARCO EN TABLERO
colocar_barco([barco], tablero)  
# OJO: lo envolvemos en lista si tu función espera lista de barcos

print("\n🔹 TABLERO CON BARCO")
print(tablero)


# 4. PEDIR COORDENADAS
print("\n🔹 AHORA VAMOS A DISPARAR")

fila, columna = ask_coord()


# 5. DISPARAR
tablero = disparar(fila, columna, tablero)

print("\n🔹 TABLERO DESPUÉS DEL DISPARO")
print(tablero)