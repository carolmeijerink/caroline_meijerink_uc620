

## este já consegui sem IA! =D yayy

fibo = [0] * 60

fibo[0] = 0
fibo[1] = 1

for i in range(2, len(fibo)):
    fibo[i] = (fibo[i-1]) + fibo[i-2]

    

print(fibo)

    