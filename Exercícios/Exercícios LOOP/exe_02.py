
pares=""
impares=""


num1=int(input("Qual é o número 1? "))
num2=int(input("Qual é o número 2? "))
num3=int(input("Qual é o número 3? "))
num4=int(input("Qual é o número 4? "))
num5=int(input("Qual é o número 5? "))
num6=int(input("Qual é o número 6? "))
num7=int(input("Qual é o número 7? "))
num8=int(input("Qual é o número 8? "))
num9=int(input("Qual é o número 9? "))
num10=int(input("Qual é o número 10? "))

nums=[num1,num2,num3,num4,num5,num6,num7,num8,num9,num10]




print("Números pares: ")

for num in nums:
    if num % 2 == 0:
        print(num, end=" | ")


print("\n\nNúmeros ímpares: ")

for num in nums:
    if num % 2 != 0:
        print(num, end=" | ")
