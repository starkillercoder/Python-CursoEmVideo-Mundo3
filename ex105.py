ficha = dict()
def notas(*n, sit=False):
    """
    Calcula a média do aluno e (opcional) mostra a situação
    :param n: valores das notas
    :param sit: se sit=True: mostra a situação, se sit=False: não mostra
    :return: retorna a média
    """
    ficha['total'] = len(n)
    ficha['maior'] = max(n)
    ficha['menor'] = min(n)
    ficha['média'] = sum(n) / len(n)
    if sit:
        if ficha['média'] >= 7:
            ficha['situação'] = 'BOA'
        if ficha['média'] < 5:
            ficha['situação'] = 'RUIM'
        else:
            ficha['situação'] = 'RAZOÁVEL'
    return ficha
resp = notas(3.5, 2, 6.5, 2, 7, 4, sit=True)
print(resp)
