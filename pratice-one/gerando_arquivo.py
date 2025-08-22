texto_para_gravar = "Texto"

with open("arquivo_text.text", mode="w", encoding="UTF-8") as arquivo:
    arquivo.write(texto_para_gravar)

print("O arquivo foi Gravado!")

