#* Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
 #* Podrás configurar generar contraseñas con los siguientes parámetros:
 #* - Longitud: Entre 8 y 16.
 #* - Con o sin letras mayúsculas.
 #* - Con o sin números.
 #* - Con o sin símbolos.
 #* (Pudiendo combinar todos estos parámetros entre ellos)

import random
import string
def generar(cant, may, n, sim,password):
    i=0
    p=[]
    while i<= cant:
        if may:
            p.append(string.ascii_uppercase)
            password.append(random.choices(p,k=cant))
            print(password)
        if n:
            p.append(string.digits)
            password.append(random.choices(p,k=cant))
            print(password)
        if sim:
            p.append(string.punctuation)
            password.append(random.choices(p,k=cant))
            print(password)
    return password

cant = int(input("cantidad de caracteres: "))
password = []
may= input("Quiere mayusculas [y/n]?")
if may == 'y':
    may = True
elif may == 'n':
    may = False
else:
    print("Error")
n=input("Quiere numeros? [y/n]")
if n == 'y':
    n = True
elif n == 'n':
    n = False
else:
    print("Error")
sim=input("quiere simbolos? [y/n]")
if sim == 'y':
    sim = True
elif sim == 'n':
    sim = False
else:
    print("Error")

print(generar(cant,may,n,sim,password))