# * Escribe un programa que muestre cómo transcurre un juego de tenis y quién lo ha ganado.
 #* El programa recibirá una secuencia formada por "P1" (Player 1) o "P2" (Player 2), según quien
 #* gane cada punto del juego.
 #* 
 #* - Las puntuaciones de un juego son "Love" (cero), 15, 30, 40, "Deuce" (empate), ventaja.
 #* - Ante la secuencia [P1, P1, P2, P2, P1, P2, P1, P1], el programa mostraría lo siguiente:
 #*   15 - Love
 #*   30 - Love
 #*   30 - 15
 #*   30 - 30
 #*   40 - 30
 #*   Deuce
 #*   Ventaja P1
 #*   Ha ganado el P1
 #* - Si quieres, puedes controlar errores en la entrada de datos.   
 #* - Consulta las reglas del juego si tienes dudas sobre el sistema de puntos.   

import random
def partido():
    lista = [1,1,2,2,1,2,1,1]
    jugador1 = "Love"
    jugador2 = "Love"
    for i in range(len(lista)):
        print(lista[i])
        if lista[i] == 1:
            if jugador1 == "Love":
                jugador1=15
            elif jugador1 == 15:
                jugador1 = 30
            elif jugador1 == 30:
                jugador1 =40
            elif jugador1 == 40 and jugador2 == 40:
                jugador1="Ventaja"
            elif jugador1 == 40 and jugador2 == "Ventaja":
                jugador2,jugador1 = "deuce"
            elif jugador1 == "deuce":
                jugador1 = "Ventaja"
            else:
                jugador1="Ganador"
        else:
            if jugador2 == "Love":
                jugador2=15
            elif jugador2 == 15:
                jugador2 = 30
            elif jugador2 == 30:
                jugador2 =40
            elif jugador2 == 40 and jugador1 == 40:
                jugador2="Ventaja"
            elif jugador2 == 40 and jugador1 == "Ventaja":
                jugador2,jugador1 = "deuce"
            elif jugador2 == "deuce":
                jugador2 = "Ventaja"
            else:
                jugador2="Ganador"
        print(f"J 1 {jugador1} --- J 2 {jugador2}")
partido()