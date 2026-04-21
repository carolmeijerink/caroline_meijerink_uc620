palavras = ["PYthon", "banana", "CÓDIGO", "intELIGENTE", "dados"]

def contagem_minusculas(palavra):
    contagem = 0
    for letra in palavra:
        if 97 <= ord(letra) <= 122:
            contagem += 1
    return contagem

n = len(palavras)
for i in range(n):
    for j in range(0, n - i - 1):
        if contagem_minusculas(palavras[j]) > contagem_minusculas(palavras[j + 1]):
            palavras[j], palavras[j + 1] = palavras[j + 1], palavras[j]

print(palavras)
