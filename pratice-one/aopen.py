with open("arquivo_text.text", mode="r", encoding="UTF-8") as arquivo:
    conteudo = arquivo.read().splitlines()

print(conteudo)