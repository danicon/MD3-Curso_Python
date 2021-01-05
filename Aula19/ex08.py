from datetime import date

cadastro = dict()
ano = date.today().year

cadastro['nome'] = str(input('Nome: '))
nasceu = int(input('Ano de nascimento: '))
nascimento = ano - nasceu
cadastro['idade'] = nascimento
cadastro['ctps'] = int(input('Carteira de trabalho (0 não tem): '))
if cadastro['ctps'] > 0:
    contratado = int(input('Ano de contratação: '))
    cadastro['contratação'] = contratado
    cadastro['salario'] = float(input('Salário: R$'))
    cadastro['aposentadoria'] = (35 - (ano - contratado)) + nascimento

print(30*'-=')
print(cadastro)
for k, v in cadastro.items():
    print(f'{k} tem o valor {v}')