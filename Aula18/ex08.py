from random import randint
mega = []
sorteio = []
jogos = int(input('Quantos jogos você quer que eu sortei? '))
cont = 1 
while cont < jogos:
    for c in range(0, 6):
        sorte = randint(1, 60)
        sorteio.append(sorte)
        mega.append(sorteio[:])
        sorteio.clear()
    cont += 1
    

print(sorteio)
print(mega)