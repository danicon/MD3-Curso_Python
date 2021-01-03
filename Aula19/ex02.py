pessoas = {'nome': 'Daniel', 'sexo': 'M', 'idade': 19}
pessoas['nome'] = 'Leandro'
pessoas['peso'] = 98.5
del pessoas['sexo']
for k, v in pessoas.items():
    print(f'{k} = {v}')