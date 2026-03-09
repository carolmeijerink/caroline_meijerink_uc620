


status = "ok"
tempo_resposta = 234

match status:
    case "ok" if tempo_resposta > 200:
        print("Servidor lento")
    case "ok":
        print("Servidor ativo")
    case "erro":
        print("Servidor indisponível")
    case _:
        print("Estado desconhecido")