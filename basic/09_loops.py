# Loops

my_condition = 0

while my_condition <10 :
    my_condition += 1
    print ( my_condition)
else: 
    print("paso")

my_condition2 = 0

while my_condition2 <10 :
    my_condition2 += 1
    print(my_condition2)
    if my_condition2 == 5:
        print("paro")
        break

#For

my_list = [1,2,3,4,5,6,7,8,9,100]

for element in my_list:
    print(element)

my_dict= {"name":"manu", "apellido":"pena" }

for element in my_dict.values():
    print(element)

