

mensagem = input("Escreva a sua mensagem: ")

match mensagem:
    case "olá" | "bom dia":
        print("Saudação")
    case m if m.endswith("?"):
        print("A mensagem é uma pergunta")
    case m if "tchau" in m or "adeus" in m:
        print("Despedida")
    case _:
        print("Mensagem genérica")