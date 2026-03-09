
nota = int(input("Digite a nota (0-100): "))

match nota:
    case n if n >= 90:
        print("Excelente")
    case n if n >= 70 and n < 90:
        print("Bom")
    case n if n >= 50 and n < 70:
        print("Suficiente")
    case _:
        print("Insuficiente")