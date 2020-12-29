cadastro = [[], []]

for c in range(0, 7):
    num = int(input(f'Digite o {c+1}° valor: '))
    if num % 2 == 0:
        cadastro[0].append(num)
    else:
        cadastro[1].append(num)

print(30*'-=')
cadastro[0].sort()
cadastro[1].sort()
print(f'Os valores pares digitados foram: {cadastro[0]}')
print(f'Os valores ímpares digitados foram: {cadastro[1]}')
