#Strings

my_string = "Hola"

my_other_string = "Python"

print(my_string + " "+ my_other_string) #concatenacion

#\n salto de linea
#\t tabulacion

#Formateo
name, age="manuel", 28

print("mi nombre es {} y edad {}".format(name,age))
print("mi nombre es %s y edad %d" %(name,age))
print(f"mi nombre es {name}, y edad {age}")


#Desempaquetado

language = "Python"

language_slice = language [1:3]
print(language_slice)

#Reverse
reversed_language = language[::-1]
print(reversed_language)

#Funciones
print(language.capitalize()) #primera mayuscula
print(language.upper()) #todoo mayuscula
print(language.count("h")) #cuenta esa letra
#etc



