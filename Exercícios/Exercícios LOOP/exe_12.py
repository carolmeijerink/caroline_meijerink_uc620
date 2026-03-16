

num = int(input("Introduza o número deseja calcular: "))

cont = 0 

for i in range (1, num):
    print ("Cálculos com o número ", i, ": ")
    
    soma = num + i
    sub = num - i
    mult = num * i
    div = num / i

    cont += 4

    print("Soma: ", soma, " | Subtração: ", sub, " | Mutiplicação :", mult, " | Divisão :", div, "\n***")

print ("Total de operações efetuadas: ", cont)

