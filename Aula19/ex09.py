jogador = dict()
partidas = list()
p = tot = 0
jogador['nome'] = str(input('Nome do Jogador: '))
quant = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
while p < quant:
    jogos = int(input(f'Quantos gols na partida {p}? '))
    partidas.append(jogos)
    tot += jogos
    p += 1
jogador['gols'] = partidas
jogador['total'] = tot
print(jogador)