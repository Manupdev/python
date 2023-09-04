#Funciones de orden superior

def sum_one(value):
    return value +1

def sum_two_values_and_add_one(first_value, second_value):
    return sum_one(first_value + second_value)


def sum_two_values_and_add_one(first_value, second_value,sum_one):
    return sum_one(first_value + second_value)

def sum_five(value):
    return value + 5

print(sum_two_values_and_add_one(5,2,sum_one))
print(sum_two_values_and_add_one(5,2,sum_five))


def sum_ten():
    def add(value):
        return value+10
    return add

add_closure = sum_ten()
(print(add_closure(5)))


#Built-in

numbers= [2,5,10,21,3,30]
#Map

def multiply_two(number):
    return number * 2

print(list(map(multiply_two, numbers)))
print(list(map(lambda number:number *2, numbers)))

#Filter

def filter_greater_than_ten(number):
    if number > 10:
        return True
    return False

print(list(filter(filter_greater_than_ten, numbers)))
print(list(filter(lambda number:number >10, numbers)))

#Reduce
from functools import reduce

def sum_two_values(first, second):
    print(first)
    print(second)
    return first + second


print(reduce(sum_two_values,numbers))
