# 1. Múltiplos de 3 e 5

# Escreva uma função que, dado n, some todos os números menores que n que sejam múltiplos de 3 ou 5.
# Exemplo:
# n = 10 → 23 (3 + 5 + 6 + 9)

def multiplos(n):
    soma = 0
    for i in range(n):
        if i % 3 == 0 or i % 5 == 0:
            soma += i
    return soma
print(multiplos(10))



