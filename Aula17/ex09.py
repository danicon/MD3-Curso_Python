expr = str(input('Digite a expressão: '))
pilha = []
for simb in expr:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressão está válida!')
else:
    print('Sua expressão está errada!')

# OU

# exp = str(input('Digite a expressão: ')).split()
# parent = parentc = 0
# for c in exp:
#     for e in c:
#         if e == '(':
#             parent += 1
#         elif e == ')':
#             parentc += 1
# if parent == parentc:
#     print('Sua expressão está válida!')
# else:
#     print('Sua expressão está errada!')