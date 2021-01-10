def contador(*num):
    for valor in num:
        print(f'{valor} ', end='')
    print('FIM!')

contador(2, 1, 7)
contador(8, 8)
contador(4, 4, 7, 6, 2)