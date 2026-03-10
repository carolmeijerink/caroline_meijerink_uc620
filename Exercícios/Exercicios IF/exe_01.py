print("Qual valor, em segundos, pretendes converter?")

seg=int(input())

horas= seg // 3600

seg= seg % 3600

minutos= seg // 60

seg = seg % 60

print(f"O valor convertido é igual a {horas} horas, {minutos} miutos e {seg} segundos.")