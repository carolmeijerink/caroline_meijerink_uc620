
num1 = int(input("Qual é o número 1? "))
num2 = int(input("Qual é o número 2? "))
num3 = int(input("Qual é o número 3? "))

if num1>num2 and num2>num3:
    print(f"Crescente: {num3}, {num2}, {num1}. \nDecrescente: {num1}, {num2}, {num3}")

elif num1>num3 and num3>num2:
    print(f"Crescente: {num2}, {num3}, {num1}. \nDecrescente: {num1}, {num3}, {num2}.")

elif num2>num1 and num1>num3:
    print(f"Crescente: {num3}, {num1}, {num2}. \nDecrescente: {num2}, {num1}, {num3}.")

elif num2>num3 and num3>num1:
    print(f"Crescente: {num1}, {num3}, {num2}. \nDecrescente: {num2}, {num3}, {num1}.")

elif num3>num1 and num1>num2:
    print(f"Crescente: {num2}, {num1}, {num3}. \nDecrescente: {num3}, {num1}, {num2}.")

elif num3>num2 and num2>num1:
    print(f"Crescente: {num1}, {num2}, {num3}. \nDecrescente: {num3}, {num2}, {num1}.")



elif num1==num2==num3:
    print(f"Os números são iguais.")