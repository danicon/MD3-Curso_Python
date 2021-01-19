def notas(*n, sit=False):
    """
    -> Funcao para analisar notas e situacoes de varios alunos.
    :param n: Uma ou mais notas e situacoes dos alunos (aceita varias)     
    :param sit: Valor opcional, indicando se deve ou nao adicionar a siuacao
    :return: Dicionario com varias informacoes sobre a situacao da turma.
    """
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['média'] = sum(n)/len(n)
    if sit:
        if r['média'] >= 7:
            r['situação'] = 'BOA'
        elif r['média'] >= 5:
            r['situação'] = 'RAZOÁVEL'
        else:
            r['situação'] = 'RUIM'
    return r


resp = notas(5.5, 2.5, 1.5, sit=True)
print(resp)
help(notas)


# Ou


# def notas(*nums, sit = False):
#     """
#     -> Funcao para analisar notas e situacoes de varios alunos.
#     :param n: Uma ou mais notas e situacoes dos alunos (aceita varias)
#     :param sit: Valor opcional, indicando se deve ou nao adicionar a siuacao
#     :return: Dicionario com varias informacoes sobre a situacao da turma.
#     """
#     print(30*'-')
#     tot = mai = men = soma = 0
#     for n in nums: 
#         if tot == 0:
#             mai = n
#             men = n
#         else:
#             if n > mai:
#                 mai = n
#             if n < men:
#                 men = n
#         soma += n
#         tot += 1
#     med = soma / tot  
#     boletim = {'total': tot, 'maior': mai, 'menor': men, 'média': med}
#     if sit:
#         if med < 5:
#             boletim['situação'] = 'RUIM'
#         elif med < 7:
#             boletim['situação'] = 'RAZOÁVEL'
#         else:
#             boletim['situação'] = 'BOA'
#     return boletim


# resp = notas(3.5, 2, 6.5, 2, 7, 4, sit=True)
# print(resp)
# help(notas)