# Lista Compresion


my_original_list = [35,24,62,52,30,30,17]

my_list = [i for i in range(8)]
my_list2 = [i+1 for i in range(8)]
my_list3 = [i*2 for i in range(8)]

print(my_list)
print(my_list2)
print(my_list3)


def sum_five(number):
    return number + 5

my_list4 = [sum_five(i) for i in range(8)]
print(my_list4)