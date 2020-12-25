listval = []
while True:
    listval.append(int(input('Digite um valor: ')))
    r = str(input('Quer continuar? [S/N] '))
    if r in 'Nn':
        break
print(30*'-=')
print(f'Você digitou {len(listval)} elementos.')

print(f'Os valores em ordem decrescente são ')
for l in listval:
    if l == 5:
        parte = 'O valor 5 faz parte da lista!'
    else:
        parte = 'O valor 5 não faz parte da lista!'
print(parte)
