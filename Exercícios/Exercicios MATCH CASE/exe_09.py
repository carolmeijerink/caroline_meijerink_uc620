
metodo = "GET"
conteudo = ""

match metodo:
    case "GET":
        print("Requisição GET recebida")
    
    case "POST" if conteudo != "":
        print("Requisição POST com dados válidos")
    
    case "POST" if conteudo == "":
        print("Requisição POST sem dados")
        
    case _:
        print("Método não suportado")