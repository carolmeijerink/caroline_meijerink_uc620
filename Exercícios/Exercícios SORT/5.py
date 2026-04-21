
palavras = ["banana", "bola", "abacaxi", "arroz", "uva", "urso"]


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


def agrupar_e_ordenar(lista_palavras):
    dicionario_agrupado = {}

    for p in lista_palavras:
        letra_inicial = p[0].lower()
        
        if letra_inicial not in dicionario_agrupado:
            dicionario_agrupado[letra_inicial] = []
        
        dicionario_agrupado[letra_inicial].append(p)

    for letra in dicionario_agrupado:
        grupo_ordenado = sort_palavras_manual(dicionario_agrupado[letra])
        dicionario_agrupado[letra] = grupo_ordenado

    return dicionario_agrupado

resultado = agrupar_e_ordenar(palavras)

print("Resultado Final Agrupado e Ordenado:")
for letra, lista in resultado.items():
    print(f"'{letra}': {lista}")