nums = cont = []
maior = menor = 0
for num in range(0, 5):
    nums.append(int(input(f'Digite um valor para a Posição {num}: ')))
    
for cont, n in enumerate(nums):
    if cont == 0:
        maior = n
        menor = n
        ma = cont
        me = cont
    else:
        if n > maior:
            maior = n
            ma = cont
        if n < menor:
            menor = n
            me = cont


print(35*'=-')
print(f'Você digitou os valores {nums}')
print(f'O maior valor digitado foi {maior} nas posição {ma}...')
print(f'O menor valor digitado foi {menor} nas posição {me}...')
