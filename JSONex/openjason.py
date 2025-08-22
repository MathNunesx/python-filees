import json

with open("arquivo.json", mode="r", encoding="UTF-8") as arquivo:
    conteudo =  arquivo.read()

convertido = json.loads(conteudo)

print(convertido)
print(type(convertido))