jogador = dict()
partidas = list()
jogador['nome'] = str(input('Nome do jogador: '))
tot = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
for c in range(0, tot):
    partidas.append(int(input(f'    Quantos gols na partida {c}? ')))
jogador['gols'] = partidas[:]
jogador['total'] = sum(partidas)
print(30*'-=')
print(jogador)
print(30*'-=')
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print(30*'-=')
print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas.')
for i, v in enumerate(jogador["gols"]):
    print(f'  => Na partida {i}, fez {v} gols.')
print(f'Foi um total de {jogador["total"]} gols.')


# Ou

# jogador = dict()
# partidas = list()
# p = tot = 0
# jogador['nome'] = str(input('Nome do Jogador: '))
# quant = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
# while p < quant:
#     jogos = int(input(f'    Quantos gols na partida {p}? '))
#     partidas.append(jogos)
#     tot += jogos
#     p += 1
# jogador['gols'] = partidas
# jogador['total'] = tot
# print(30*'-=')
# print(jogador)
# print(30*'-=')
# for k, v in jogador.items():
#     print(f'O campo {k} tem o valor {v}')
# print(30*'-=')
# print(f'O jogador {jogador["nome"]} jogou {quant} partidas.')
# for c, g in enumerate(partidas):
#     print(f'  => Na partida {c}, fez {g} gols.')
# print(f'Foi um total de {jogador["total"]} gols.')