def aumentar(preco=0, taxa=0, formato=False):
    """
    -> Calcula o aumento de um determinado preco,
    retornando o resultado com ou sem formatacao.
    :param preco: O preco que se quer reajustar
    :param taxa: Qual e a porcentagem do aumento.
    :param formato: Quer a saida formatada ou nao?
    :return: O valor resultado, com ou sem formato
    """
    res = preco + (preco * taxa / 100)
    return res if formato is False else moeda(res)


def diminuir(preco=0, taxa=0, formato=False):
    res = preco - (preco * taxa / 100)
    return res if formato is False else moeda(res)


def dobro(preco=0, formato=False):
    res = preco * 2
    return res if not formato else moeda(res)


def metade(preco=0, formato=False):
    res = preco / 2
    return res if not formato else moeda(res)


def moeda(preco=0, moeda='R$'):
    return f'{moeda}{preco:>.2f}'.replace('.',',')
