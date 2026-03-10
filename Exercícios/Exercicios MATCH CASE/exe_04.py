
entrada = 150

match entrada:
    case int():
        print("Número inteiro")
    case float():
        print("Número decimal")
    case str() if entrada.isnumeric():
        print("String numérica")
    case str():
        print("String textual")
    case list():
        print("Lista")
    case _:
        print("Tipo desconhecido")
