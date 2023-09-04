#* Crea un programa que calcule quien gana más partidas al piedra,
 #* papel, tijera, lagarto, spock.
 #* - El resultado puede ser: "Player 1", "Player 2", "Tie" (empate)
 #* - La función recibe un listado que contiene pares, representando cada jugada.
 #* - El par puede contener combinaciones de "🗿" (piedra), "📄" (papel),
 #*   "✂️" (tijera), "🦎" (lagarto) o "🖖" (spock).
 #* - Ejemplo. Entrada: [("🗿","✂️"), ("✂️","🗿"), ("📄","✂️")]. Resultado: "Player 2".
 #* - Debes buscar información sobre cómo se juega con estas 5 posibilidades.



def juego():
    p1 = 0
    p2 = 0
    partidas = 0
    while partidas <3:
        x=int(input("Elige J1: "))
        y=int(input("Elige J2: "))
        if x == 1:
            print("Jugador 1: Piedra")
            if y == 2:
                print("Jugador 2: Papel")
                p2 +=1
            elif y == 3:
                print("Jugador 3: Tijera")
                p1 += 1
            else:
                p1 += 1
                p2 += 1
        elif x == 2:
            print("Jugador 1: Papel")
            if y == 1:
                print("Jugador 2: Piedra")
                p1 += 1
            elif y == 3:
                print("Jugador 2: Tijera")
                p2 += 1
            else:
                p1 += 1
                p2 +=1
        else:
            print("Jugador 1 : Tijera")
            if y == 1:
                print("Jugador 2: Piedra")
                p2 += 1
            elif y == 2:
                print("Jugador 2: Papel")
                p1 += 1
            else:
                p1 += 1
                p2 += 1
        partidas +=1
    if p1>p2:
        print("Gana Jugador 1")
    elif p2>p1:
        print("Gana Jugador 2")
    else:
        print("Empate")

print(juego())

