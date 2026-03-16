
num = int(input("Introduza um número para verificar quantos divisores ele possui: "))


divisores = 0
contador_divi = 1

while(contador_divi<=num):
    if(num%contador_divi == 0):
        divisores += 1
    contador_divi +=1
    
    


print("O número", num, "possui", divisores, "divisores.")

