import json

file = open("dict.txt","r")
y = file.read()

diction = json.loads(y)
file.close()