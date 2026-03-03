
num1=int(input("Qual o primeiro número para comparar? "))
num2=int(input("Qual o segundo número para comparar? "))
num3=int(input("Qual o terceiro número para comparar? "))

if num1>num2 and num2>num3:
    print(f"O maior é o {num1} e o menor é o {num3}.")

if num1>num3 and num3>num2:
    print(f"O maior é o {num1} e o menor é o {num2}.")

if num2>num1 and num1>num3:
    print(f"O maior é o {num2} e o menor é o {num3}.")

if num2>num3 and num3>num1:
    print(f"O maior é o {num2} e o menor é o {num1}.")

if num3>num1 and num1>num2:
    print(f"O maior é o {num3} e o menor é o {num2}.")

if num3>num2 and num2>num1:
    print(f"O maior é o {num3} e o menor é o {num1}.")