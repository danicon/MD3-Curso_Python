def escreva(msg):
    tam = len(msg) + 4
    print('~'*tam)
    print(f'  {msg}')
    print('~'*tam)


escreva('Gustavo Guanabara')
escreva('Curso de Python no YouTube')
escreva('CeV')


# Ou


# def escreva(var):
#     for c in range(0, len(var)+4):
#         print('~', end='')
#     print()
#     print(var)
#     for c in range(0, len(var)+4):
#         print('~', end='')
#     print()


# escreva(var = '     Gustavo Guanabara')
# escreva(var = '     Curso de Python no YouTube')
# escreva(var = '     CeV')