#* Escribe un programa que, dado un número, compruebe y muestre si es primo,
 #* fibonacci y par.
 #* Ejemplos:
 #* - Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
 #* - Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"

def paridad (n):
    if n%2 == 0:
        return True
    else:
        return False

def es_primo(n):
    b=0
    i=2
    while i<n:
        if n%i == 0:
            b=1
        i += 1
    if b == 0:
        return True
    else:
        return False 
def fibonacci(n):
    f=1
    x=0
    b=0
    if n == 0 or n == 1:
        return True
    while f <= n:
        if f == n:
            b=1
            return True
        else:
            f=f+x
            x=f-x
    if b==1:
        return True
    else:
        return False
    
n=int(input("Indica numero: "))
paridad(n)
es_primo(n)
fibonacci(n)

if paridad(n):
    print(f"{n} es par")
else:
    print(f"{n} es impar")
if es_primo(n):
    print(f"{n} es primo")
else:
    print(f"{n} no es primo")
if fibonacci(n):
    print(f"{n} es fibonacci")
else:
    print(f"{n} no es fibonacci")