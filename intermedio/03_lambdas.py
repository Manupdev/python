# Lambdas

sum_two_values = lambda first_value , second_value: first_value + second_value
print(sum_two_values(2,4))

def sum_three_values(first_value):
    return lambda first_value, second_value: first_value + second_value
