from random import randint
maior = menor = cont = 0
numeros = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print(f'Os valores sorteados foram: ', end='')

for n in numeros:
    print(f'{n} ', end='')
    if cont == 0:
        maior = n
        menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    cont += 1
print(f'\nO maior valor sorteado foi {maior}')
print(f'O menor valor sorteado foi {menor}')


# Ou print(f'\nO maior valor sorteado foi {max(numeros)}')
# print(f'O menor valor sorteado foi {min(numeros)}')
