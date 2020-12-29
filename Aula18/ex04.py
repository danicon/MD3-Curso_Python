grupo = list()
dados = list()
cont = maior = menor = 0
while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    grupo.append(dados[:]) 
    for p in grupo:
        if cont == 0:
            maior = p[1]
            menor = p[1]
        else:
            if p[1] > maior:
                maior = p[1]
            if p[1] < menor:
                menor = p[1]
    cont += 1
    dados.clear()
    r = str(input('Quer continuar? [S/N] '))
    if r in 'Nn':
        break

print(30*'-=')
print(f'Ao todo, você cadastrou {cont} pessoas.')
print(f'O maior peso foi de {maior:.1f}Kg. Peso de ', end='')
for c, m in enumerate(grupo):
    if m[1] == maior:
        print(f'[{grupo[c][0]}] ', end='')
print()
print(f'O menor peso foi de {menor:.1f}Kg. Peso de ', end='')
for c, m in enumerate(grupo):
    if m[1] == menor:
        print(f'[{grupo[c][0]}] ', end='')
print()
