# nums = []
# maior = menor = 0
# for num in range(0, 5):
#     nums.append(int(input(f'Digite um valor para a Posição {num}: ')))

# for cont, n in enumerate(nums):
#     if cont == 0:
#         maior = n
#         menor = n
#     else:
#         if n > maior:
#             maior = n
#         if n < menor:
#             menor = n

# print(35*'=-')
# print(f'Você digitou os valores {nums}')
# print(f'O maior valor digitado foi {maior} nas posição ', end='')
# for p, m in enumerate(nums):
#     if m == maior:
#         print(f'{p}... ', end='')
# print()

# print(f'O menor valor digitado foi {menor} nas posição ', end='')
# for p, m in enumerate(nums):
#     if m == menor:
#         print(f'{p}... ', end='')
# print()



listanum = []
mai = men = 0
for c in range(0, 5):
    listanum.append(int(input(f'Digite um valor para a posição {c}: ')))
    if c == 0:
        mai = men = listanum[c]
    else:
        if listanum[c] > mai:
            mai = listanum[c]
        if listanum[c] < men:
            men = listanum[c]
print('=-'*30)
print(f'Você digitou os valores {listanum}')
print(f'O maior valor digitado foi {mai} nas posições ', end='')
for i, v in enumerate(listanum):
    if v == mai:
        print(f'{i}... ', end='')
print()
print(f'O menor valor digitado foi {men} nas posições ', end='')
for i, v in enumerate(listanum):
    if v == men:
        print(f'{i}... ', end='')
print()