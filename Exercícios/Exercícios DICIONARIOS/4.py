utilizador = {'nome': 'Carlos', 'idade': 28}

email = utilizador.get('email')

if email:
    print("Email encontrado:", email)
else:
    print("Email não encontrado.")