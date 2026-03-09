

num1 = int(input("Qual é o número 1? "))
num2 = int(input("Qual é o número 2? "))

if num1>num2:
    print(f"Crescente: {num2}, {num1}. \nDecrescente: {num1}, {num2}")

elif num2>num1:
    print(f"Crescente: {num1}, {num2}. \nDecrescente: {num2}, {num1}.")

elif num1==num2:
    print(f"Os números são iguais.")