

num = int(input("Digite um número (inteiro, sem vírgulas) para verificar se é um número primo: "))

if num <= 1:
    print("Não é primo.")

else:
    contagem_divisores = 0
    divisor = 1
    
    while divisor <= num:
        if num % divisor == 0:
        
            contagem_divisores += 1
        divisor = divisor + 1

    
    if contagem_divisores == 2:
        print("O número", num, "é PRIMO!")
    else:
        print("O número", num, "NÃO é primo.")

