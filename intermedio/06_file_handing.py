#Ficheros

# .txt file

import os
txt_file = open("intermedio/my_file.txt", "r+") #Leer y escribir
#print(txt_file.read(10))

for line in txt_file.readlines():
    print(line)

txt_file.write(" \n TMb me gusta excel")


#txt_file = open("intermedio/my_file.txt", "w+")#Lo crea si no existe

#os.remove("intermedio/my_file.txt") # lo borra

#.json file

import json

json_file = open("intermedio/my_file.json", "w+")

json_test = {
    "nombre": "manu",
    "surname":"pena",
    "age":28,
    "language": ["python","Swift","Kotlin"]
}

json.dump(json_test, json_file, indent=2)


#.csv file
import csv

csv_file = open("intermedio/my_file.csv", "w+")

csv_writer = csv.writer(csv_file)
csv_writer.writerow(["name","surname","age", "language"])
csv_writer.writerow(["manu","pena",28,"python"])


#xml file
import xml

