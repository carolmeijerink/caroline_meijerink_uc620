tipo = input("Digite o tipo (compra/venda): ")
valor = input("Digite o valor: ")

match tipo:
    case "compra":
        print(f"Compra de {valor}€")
    case "venda":
        print(f"Venda de {valor}€")
    case _:
        print("Pedido desconhecido. Digite apenas 'compra' ou 'venda'.")