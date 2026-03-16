

num = int(input("Quer ver a tabuada de qual número? "))
result = 0

print()

for i in range (1,11):
    result = num * i
    print(num, " x ", i, " = ", result)
