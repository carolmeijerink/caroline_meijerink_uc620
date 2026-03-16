
nums = 10
primos = 0

num_atual = 0

print("Apresentamos os 10 primeiros números primos que existem em ordem crescente:")

while (primos < nums):

    contagem_divisores = 0
    divisor = 1
    
    while divisor <= num_atual:
        if num_atual % divisor == 0:
        
            contagem_divisores += 1
        divisor = divisor + 1

    
    if contagem_divisores == 2:
        print(num_atual)
        primos += 1
    
    num_atual += 1