

j1 = input("Jogador 1: ")
j2 = input("Jogador 2: ")

match (j1, j2):
    case (p1, p2) if p1 == p2:
        print("Empate")
    case ("pedra", "tesoura") | ("tesoura", "papel") | ("papel", "pedra"):
        print("Jogador 1 venceu")
    case ("tesoura", "pedra") | ("papel", "tesoura") | ("pedra", "papel"):
        print("Jogador 2 venceu")
    case _:
        print("Jogada inválida")