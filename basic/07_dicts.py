#Diccionarios

my_other_dict = {"Nombre":"Manu", "Apellido":"Pena", "Edad":28}

my_dict = {
    "nombre":"manu",
    "apellido" : "pena",
    "edad" : 28,
    "Lenguajes" : {"python","swift"}
}

print(my_dict["nombre"])

del my_dict["apellido"]

print(my_dict)

print("nombre" in my_dict) #Busca clave, no valor

print(my_dict.items()) #listado
print(my_dict.keys())#lista de keys
