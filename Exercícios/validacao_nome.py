def eh_valido(text):      
    for char in text:
        code = ord(char)
        
        eh_maiusculo = (65 <= code <= 90)
        eh_minusculo = (97 <= code <= 122)
        eh_espaco = (code == 32)
        
        if not (eh_maiusculo or eh_minusculo or eh_espaco):
            return False
            
    return True


def eh_ascii_maiusculo(texto):      
    for char in texto:
        code = ord(char)

        if not (65 <= code <= 90):
            return False
            
    return True


def verifica_letras_iniciais_maiusculas(texto):
    partes = texto.split(' ')

    for parte in partes:
        letra_inicial_maiuscula_parte = eh_ascii_maiusculo(parte[0])

        if not letra_inicial_maiuscula_parte:
            return False
    
    return True


while True:
    nome = input('Digite seu nome:')

    if not (eh_valido(nome)):
        print('Nome inválido: contém caracteres não permitidos.')

    elif not verifica_letras_iniciais_maiusculas(nome):
        print('Nome inválido: contém caracteres não permitidos.')

    else:
        print('Nome válido!')