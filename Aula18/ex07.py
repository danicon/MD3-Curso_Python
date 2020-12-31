matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma = scoluna = mai = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))


print(30*'-=')
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
        if matriz[l][c] % 2 == 0:
            soma += matriz[l][c]
        if c == 2:
            scoluna += matriz[l][c]
    print()

print(30*'-=')
print(f'A soma dos valores pares é {soma}')
print(f'A soma dos valores da terceira coluna é {scoluna}')
for l in range(0, 3):
    for c in range(0, 3):
        for cont, n in enumerate(matriz[l]):
            if l == 1:
                if cont == 0:
                    mai = n
                else:
                    if n > mai:
                        mai = n
        break
print(f'O maior valor da segunda linha é {mai}.')