#* Crea un programa que simule el comportamiento del sombrero selccionador del
 #* universo mágico de Harry Potter.
 #* - De ser posible realizará 5 preguntas (como mínimo) a través de la terminal.
 #* - Cada pregunta tendrá 4 respuestas posibles (también a selecciona una a través de terminal).
 #* - En función de las respuestas a las 5 preguntas deberás diseñar un algoritmo que
 #*   coloque al alumno en una de las 4 casas de Hogwarts:
 #*   (Gryffindor, Slytherin , Hufflepuff y Ravenclaw)
 #* - Ten en cuenta los rasgos de cada casa para hacer las preguntas
 #*   y crear el algoritmo seleccionador:
 #*   Por ejemplo, en Slytherin se premia la ambición y la astucia.

#Preguntas: 1-Cuantas libertadores? 2-Cuantas intercontinentales? 3-padre de tu rival? 4-tu rival se fue a la b? 5-copas internacionales?
#Respuestas 1: a-7, b-6, c-4, d-1
#Respuestas 2: a-3, b-2, c-1, d-0
#Respuestas 3: a-si, b-no, c-empate
#Respuestas 4: a-si, b-no
#Respuestas 5: a-18, b-12, c-3

respuestas = [["b,a,c,d"],["a,b,c,d"],["a,b"],["a,b"],["a,b,c"]]
preguntas = [["Cuantas libertadores?"],["Cuantas intercontinentales?"],["PAdre de tu rival? "],["Tu rival se fue a la b?"],["copas internacionales?"]]

def equipo():
    preg = 0
    while preg<=5:
        for preg in range(len(preguntas)):
            print(preguntas[preg])
            respuesta = input("Ingrese respuesta: ")
            for i in range(len(respuestas)):
                for j in respuestas[i]:
                    if respuesta == "b"

