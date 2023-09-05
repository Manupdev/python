"""
    Reto: Viernes 13
 * Crea una función que sea capaz de detectar si existe un viernes 13 en el mes y el año indicados.
 * - La función recibirá el mes y el año y retornará verdadero o falso.
"""

import calendar

def viernes13(year, month):
    if calendar.weekday(year, month, 13) == 4:
        print("hay")
    else:
        return False


year=int(input("año: "))
month = int(input("mes: "))

viernes13(year,month)