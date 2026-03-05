
nome=input("Qual o nome do cliente? ")
val_compra=float(input("Qual o valor da compra? "))
val_desconto=0
val_pagar=0

if val_compra<=200:
    val_desconto = val_compra*0.10
    val_pagar = val_compra-val_desconto

elif val_compra>=200.01 and val_compra<=500:
    val_desconto = val_compra*0.15
    val_pagar = val_compra-val_desconto

elif val_compra>500:
    val_desconto = val_compra*0.20
    val_pagar = val_compra-val_desconto


print(f"Nome: {nome} \nCompra: {val_compra} \nDesconto: {val_desconto} \nTotal a pagar: {val_pagar}")