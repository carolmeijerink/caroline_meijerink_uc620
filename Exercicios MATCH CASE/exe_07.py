


categoria = "alimento"
preco = 1500

match categoria:
    
    case "eletrónico" if preco > 1000:
        print("Produto de luxo")
    
    case "eletrónico":
        print("Produto comum")
        
    case "alimento":
        print("Produto alimentar")
        
    case _:
        print("Categoria desconhecida")