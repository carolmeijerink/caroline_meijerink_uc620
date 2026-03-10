


i=0
ifinal=int(input("Quantas notas queres introduzir? "))

notas=[0] * ifinal
total=0
media=0

print("Para ver a média das notas, por favor introduza a nota de um aluno, e continue preenchendo uma a uma até o fim (uma nota de cada vez).")

while i < ifinal:
    notas[i]=int(input(f"Nota {i+1}: "))
    total+=notas[i]
    i += 1

  

media = total / len(notas)

print(f"A média das notas é {media}")
