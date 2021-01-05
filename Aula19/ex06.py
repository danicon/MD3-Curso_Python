result = {}

result['nome'] = str(input('Nome: '))
result['media'] = float(input(f'Média do {result["nome"]}: '))

if result['media'] >= 7:
    result['situacao'] = 'Aprovado'
elif 5 <= result['media'] < 7:
    result['situacao'] = 'Recuperação'
else:
    result['situacao'] = 'Reprovado'
print(30*'-=')
for k, v in result.items():
    print(f'  - {k} é igual a {v}')
