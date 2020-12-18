listabr = ('São Paulo', 'Atlético - MG', 'Flamengo', 'Palmeiras', 'Internacional', 'Grêmio', 'Fluminense', 'Santos', 'Atlético - GO', 'Corinthians', 'Ceará', 'Red Bull Bragantino', 'Fortaleza', 'Athletico Paranaense', 'Sport', 'Bahia', 'Vasco da Gama', 'Coritiba', 'Goiás', 'Botafogo')

for c in range(0, len(listabr)):
    if listabr[c] == 'Corinthians':
        x = c

print(30*'-=')
print(f'Lista de times do Brasileirão: {listabr}')
print(30*'-=')
print(30*'-=')
print(f'Os 5 primeiros são {listabr[:5]}')
print(30*'-=')
print(30*'-=')
print(f'Os 4 últimos são {listabr[-4:]}')
print(30*'-=')
print(30*'-=')
print(f'Times em ordem alfabética: {sorted(listabr)}')
print(30*'-=')
print(30*'-=')
print(f'O Corinthians está na {x+1}ª posição')
# Ou print(f'O Corinthians está na {listabr.index("Corinthians")+1}ª posição')
print(30*'-=')