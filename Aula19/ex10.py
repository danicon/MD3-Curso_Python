grupo = list()
pessoas = dict()
cont = soma = media = 0
while True:
    pessoas['nome'] = str(input('Nome: '))
    pessoas['sexo'] = str(input('Sexo: [M/F] ')).upper()
    pessoas['idade'] = int(input('Idade: '))
    soma += pessoas['idade']
    grupo.append(pessoas.copy())
    cont += 1

    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break
media = soma / cont
print(grupo)
print(30*'-=')
print(f'- O grupo tem {cont} pessoas.')
print(f'- A média de idade é de {media:.2f} anos.')
print(f'- As mulheres cadastradas foram: ', end='')

for k, v in pessoas.items():
    if k == 'sexo' and v == 'F':
        print(pessoas['nome'], end=' ')
print()

print(f'- Lista das pessoas que estão acima da média:')

for k, v in pessoas.items():
    if pessoas['idade'] > media:
        print(pessoas)
