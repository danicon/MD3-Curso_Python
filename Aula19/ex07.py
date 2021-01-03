from random import randint

sort = {}
sort['jg1'] = randint(1, 6)
sort['jg2'] = randint(1, 6)
sort['jg3'] = randint(1, 6)
sort['jg4'] = randint(1, 6)

for k, v in len(sort.items()):
    print(f'{k} = {v}')
