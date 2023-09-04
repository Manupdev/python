#Funciones

def my_function ():
    print("Esto es Funcion")

my_function()

def sum_two_values (first_number , second_number):
    print(first_number + second_number)

sum_two_values(2,3)

def sum_two_values_with_return (first_number, second_number):
    return first_number + second_number

my_result = sum_two_values_with_return(10, 5)
print(my_result)

def print_name (name, surname):
    print(f"{name}, {surname}")

print_name("manu", "pena")


def print_name_with_default(name, surname = "Pena"):
    print(f"{name}, {surname}")

print_name_with_default("")

def print_texts (*text): 
    print(text)

print_texts("Hola", "Mas", "de", "un", "texto")

