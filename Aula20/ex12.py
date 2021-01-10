from random import randint
from time import sleep
lista = list()

def sorteia():  
    print('Sorteando 5 valores da lista: ', end='')
    for s in range(0, 5):
        sort = randint(0, 10)
        print(f'{sort} ', end='', flush=True)
        sleep(0.5)
        lista.append(sort)
    print('PRONTO!')


sorteia()

def somaPar(lista):
    soma = 0
    for p in lista:
        if p % 2 == 0:
            soma += p
    print(f'Somando os valores pares de {lista}, temos {soma}')


somaPar(lista)
