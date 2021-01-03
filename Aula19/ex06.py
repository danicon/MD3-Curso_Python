result = {}

result['nome'] = str(input('Nome: '))
result['media'] = float(input(f'Média do {result["nome"]}: '))

if result['media'] >= 7.0:
    result['situacao'] = 'Aprovado'
else:
    result['situacao'] = 'Reprovado'

print(f'Nome é igual a {result["nome"]}')
print(f'Média é igual a {result["media"]}')
print(f'Situação é igual a {result["situacao"]}')
