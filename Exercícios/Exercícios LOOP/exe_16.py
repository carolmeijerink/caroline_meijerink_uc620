

nums = [0] * 30
soma = 0
media=0

for i in range(len(nums)):
    nums[i] = int(input(f"Introduza o número {i+1}: "))
    soma += nums[i]


## print(nums)

media = soma / len(nums)

print(f"A média dos números inseridos é {media}")