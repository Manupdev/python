#Expresiones regulares

import re
my_string = "Expresiones regulares"
my_other_string = "leccion 7"



print(re.match("Expresiones", my_string))
match = re.match("Expresiones", my_string, re.I)
print(match)
start, end = match.span()
print(my_string[start:end])


#search

search = re.search("Expres", my_string, re.I)
print(search)

#findall

findall = re.findall("Expresion", my_string, re.I)
print(findall)

#split

print(re.split("s", my_string))

#sub
print(re.sub("Expresiones", "EXPRESIONES", my_string))

#Patterns

pattern = r"[eE]xpresiones"
print(re.findall(pattern,my_string))

#para aprender y validar expresiones regulares: https://regex101.com


