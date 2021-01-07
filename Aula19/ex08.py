from datetime import datetime
dados = dict()
dados['nome'] = str(input('Nome: '))
nasc = int(input('Ano de Nascimento: '))
dados['idade'] = datetime.now().year - nasc
dados['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))
if dados['ctps'] != 0:
    dados['contratação'] = int(input('Ano de Contratação: '))
    dados['salario'] = float(input('Salário: R$'))
    dados['aposentadoria'] = dados['idade'] + ((dados['contratação'] + 35) - datetime.now().year)
print(30*'-=')
for k, v in dados.items():
    print(f' - {k} tem o valor {v}')


# Ou

# from datetime import date

# cadastro = dict()
# ano = date.today().year

# cadastro['nome'] = str(input('Nome: '))
# nasceu = int(input('Ano de nascimento: '))
# nascimento = ano - nasceu
# cadastro['idade'] = nascimento
# cadastro['ctps'] = int(input('Carteira de trabalho (0 não tem): '))
# if cadastro['ctps'] > 0:
#     contratado = int(input('Ano de contratação: '))
#     cadastro['contratação'] = contratado
#     cadastro['salario'] = float(input('Salário: R$'))
#     cadastro['aposentadoria'] = (35 - (ano - contratado)) + nascimento

# print(30*'-=')
# for k, v in cadastro.items():
#     print(f' - {k} tem o valor {v}')