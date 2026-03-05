
saldo_inicial = int(input("Qual o saldo inicial? "))
val_cheque = int(input("Qual o valor do cheque? "))
saldo_final= saldo_inicial - val_cheque

if val_cheque>saldo_inicial:
    print("Não foi possível descontar o cheque. Saldo insuficiente.")

else:
    print(f"Cheque descontado com sucesso. Saldo: {saldo_final}.")