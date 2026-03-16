
stop = False
num_indicado = int(input("Introduza um número entre 1 e 100: "))

while stop == False:

    if num_indicado>=1 and num_indicado<=100:
        stop = True
    else:
        print("Numéro inválido.")
        num_indicado = int(input("Introduza um número entre 1 e 100: "))


print("Sucesso. O número introduzido está dentro do intervalo permitido.")

