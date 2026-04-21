nomes = [
    "Pedro Pereira",
    "Ana Beatriz",
    "Ana Clara",
    "Carlos Silva",
    "Beatriz Souza",
    "Ana Paula",
    "Pedro Andrade"
]

for i in range(len(nomes)):
    for j in range(0, len(nomes) - i - 1):

        nome_atual = nomes[j]
        proximo_nome = nomes[j + 1]

        tamanho_menor = len(nome_atual)
        if len(proximo_nome) < tamanho_menor:
            tamanho_menor = len(proximo_nome)

        trocar = False

        for k in range(tamanho_menor):
            char1 = ord(nome_atual[k])
            char2 = ord(proximo_nome[k])

            if char1 > char2:
                trocar = True
                break

            elif char1 < char2:
                trocar = False
                break

        if nome_atual[:tamanho_menor] == proximo_nome[:tamanho_menor]:
            if len(nome_atual) > len(proximo_nome):
                trocar = True

        if trocar == True:
            nomes[j] = proximo_nome
            nomes[j+1] = nome_atual

print("Lista Ordenada:")
for n in nomes:
    print(n)
