
## não consegui fazer sem ajuda da IA... #imsorry

num = int(input("Até qual limite deseja verificar os números perfeitos? "))
quant_perf = 0

print(f"\nNo intervalo de 1 a {num} são números perfeitos: ")


for i in range(2, num +1):
      
    divisor = 0
    soma_divisores= 0
    
   
    for divisor in range(1, i):
        if i % divisor == 0:
            soma_divisores += divisor

    if soma_divisores == i:
        print(i, end=" | ")
        quant_perf += 1

print(f"\n\nExistem {quant_perf} números perfeitos neste intervalo.\n")