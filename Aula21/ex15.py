from time import sleep
def ajuda(com):
    titulo(f'Acessando o manual do comando \'{com}\'')
    help(com)
    sleep(2)


def titulo(msg):
    tam = len(msg) + 4
    print('~'*tam)
    print(f'  {msg}')
    print('~'*tam)
    sleep(1)


comando = ''
while True:
    titulo('SISTEMA DE AJUDA PyHELP')
    comando = str(input('Função ou Biblioteca > '))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
titulo('ATÉ LOGO!')