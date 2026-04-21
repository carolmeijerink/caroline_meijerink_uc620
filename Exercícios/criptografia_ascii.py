def calcular_valor_chave(chave):
    return sum(ord(char) for char in chave)

def criptografar(mensagem: str, chave: str):
    valor_chave = calcular_valor_chave(chave)
    resultado = []
    
    for char in mensagem:
        codigo_original = ord(char)
        
        novo_codigo = 32 + (codigo_original - 32 + valor_chave) % 224 # 224 para poder usar intervalo com letras acentuadas (á é ...)
        resultado.append(novo_codigo)
        
    return resultado

def descriptografar(codigos: list[int], chave: str):
    valor_chave = calcular_valor_chave(chave)
    mensagem_original = ''
    
    for codigo in codigos:
        codigo_original = 32 + (codigo - 32 - valor_chave) % 224
        mensagem_original += chr(codigo_original)
        
    return mensagem_original


def texto_encriptado(codigos):
    texto_visivel = ''

    for codigo in codigos:
        texto_visivel = texto_visivel + chr(codigo)

    return texto_visivel

def listar_resultados(mensagem, chave, encriptado):
    soma_chave = sum(ord(c) for c in chave)

    print('\n' + '='*30)
    print(f'Mensagem Original: {mensagem}')
    print(f'Chave: "{chave}" (Soma ASCII: {soma_chave})')
    print(f'Códigos Gerados: {encriptado}')
    print(f'Texto Encriptado (ASCII): {texto_encriptado(encriptado)}')
    print('='*30)


while True:
    msg = input('Introduza a mensagem: ')
    chave = input('Introduza a chave: ')

    if not chave:
        print('A chave não pode estar vazia')

    else:

        codigos_num = criptografar(msg, chave)
        listar_resultados(msg, chave, codigos_num)

        decifrado = descriptografar(codigos_num, chave)
        print(f'Verificação (Descriptografado): {decifrado}')
