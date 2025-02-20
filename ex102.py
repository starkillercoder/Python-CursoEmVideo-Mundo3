def fatorial(n, show=False):
    """
    Mostra o fatorial de um número
    :param n: valor a ser calculado o fatorial
    :param show: True: Mostra a equação. False: Não mostra a equação
    :return: retorna o valor da equação
    """
    f = 1
    for c in range(n, 0, -1):
        f *= c
        if show == True:
            print(f'{c}', end=' ')
            if c > 1:
                print('x', end=' ')
            else:
                print('=', end=' ')
    return f


print('-' * 30)
print(fatorial(5, show=True))
help(fatorial)
