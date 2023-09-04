# Clases

class Person:
    def __init__(self,name,surname): #constructor de clase
        self.name = name
        self.apellido = surname
    def walk(self):
        print(f"{self.name} esta caminando")

my_person = Person("manu", "pena")
print(my_person.name)
print(my_person.apellido)
my_person.walk()

my_other_person = Person("perdo", "123")
print(my_other_person.apellido)

