from time import sleep
def maior(* nums):
    print(40*'-=')
    print('Analisando os valores passados...')
    quant = len(nums)
    mai = 0
    for c, m in enumerate(nums):
        print(f'{m} ', end='', flush=True)
        sleep(0.5)
        if c == 0:
            mai = m
        else:
            if m > mai:
                mai = m
    
    print(f'Foram informados {quant} valores ao todo.')
    print(f'O maior valor informado foi {mai}.')


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()