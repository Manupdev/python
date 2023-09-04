#Excepciones

numero1 = 5
numero3 = 1
numero2 = "1"

try:
    print(numero1 + numero2)
except:
    print("Error")


try:
    print(numero1+numero3)
    print("correcto")
except:
    print("Error")
else:
    #se ejecuta si no se produce excepcion
    print("ejecucion continua")
finally:
    #se ejecuta siempre
    print("continua")

try:
    print(numero1+numero2)
except ValueError:
    print("Errorrrrrr value error")
except TypeError:
    print("error type error")


try:
    print(numero1+numero2)
except ValueError as error:
    print(error)


