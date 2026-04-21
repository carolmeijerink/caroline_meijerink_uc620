palavra = 'algoritmo'


def ordem_alfabetica(p1, p2):
    tamanho_minimo = min(len(p1), len(p2))

    for i in range(tamanho_minimo):
        v1 = ord(p1[i])
        v2 = ord(p2[i])

        if v1 < v2:
            return True
        if v1 > v2:
            return False

    return len(p1) > len(p2)


def sort_palavras_manual(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):

            if not ordem_alfabetica(lista[j], lista[j+1]):
                lista[j], lista[j+1] = lista[j+1], lista[j]
    return lista

letras = []

for letra in palavra:
    letras.append(letra)

letras_sorted = sort_palavras_manual(letras)

def juntar_letras_em_palavra(letras):
    palavra = ''

    for letra in letras:
        palavra += letra

    return palavra

print(f"Resultado: {juntar_letras_em_palavra(letras_sorted)}")
