num = []
pares = []
impares = []
while True:
    num.append(int(input('Digite um valor: ')))
    r = str(input('Quer continuar? [S/N] '))
    if r in 'Nn':
        break
for c in num:
    if c % 2 == 0:
        pares.append(c)
    else:
        impares.append(c)
print(30*'-=')
print(f'A lista completa é {num}')
print(f'A lista de pares é {pares}')
print(f'A lista de ímpares é {impares}')