listval = []
while True:
    listval.append(int(input('Digite um valor: ')))
    r = str(input('Quer continuar? [S/N] '))
    if r in 'Nn':
        break
print(30*'-=')
print(f'Você digitou {len(listval)} elementos.')
listval.sort(reverse=True)
print(f'Os valores em ordem decrescente são {listval}')
if 5 in listval:
    print(f'O valor 5 faz parte da lista!')
else:
    print(f'O valor 5 não faz parte da lista!')