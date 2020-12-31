temp = []
princ = []
mai = men = 0
while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))
    if len(princ) == 0:
        mai = men = temp[1]
    else:
        if temp[1] > mai:
            mai = temp[1]
        if temp[1] < men:
            men = temp[1]
    princ.append(temp[:])
    temp.clear()
    resp = str(input('Quer continuar? '))
    if resp in 'Nn':
        break

print('-='*30)
print(f'Ao todo, você cadastrou {len(princ)} pessoas.')
print(f'O maior peso foi de {mai}Kg. Peso de ', end='')
for p in princ:
    if p[1] == mai:
        print(f'[{p[0]}] ', end='')
print()
print(f'O menor peso foi de {men}Kg. Peso de ', end='')
for p in princ:
    if p[1] == men:
        print(f'[{p[0]}] ', end='')
print()


# Ou


# grupo = list()
# dados = list()
# cont = maior = menor = 0
# while True:
#     dados.append(str(input('Nome: ')))
#     dados.append(float(input('Peso: ')))
#     grupo.append(dados[:]) 
#     for p in grupo:
#         if cont == 0:
#             maior = p[1]
#             menor = p[1]
#         else:
#             if p[1] > maior:
#                 maior = p[1]
#             if p[1] < menor:
#                 menor = p[1]
#     cont += 1
#     dados.clear()
#     r = str(input('Quer continuar? [S/N] '))
#     if r in 'Nn':
#         break

# print(30*'-=')
# print(f'Ao todo, você cadastrou {cont} pessoas.')
# print(f'O maior peso foi de {maior:.1f}Kg. Peso de ', end='')
# for c, m in enumerate(grupo):
#     if m[1] == maior:
#         print(f'[{grupo[c][0]}] ', end='')
# print()
# print(f'O menor peso foi de {menor:.1f}Kg. Peso de ', end='')
# for c, m in enumerate(grupo):
#     if m[1] == menor:
#         print(f'[{grupo[c][0]}] ', end='')
# print()
