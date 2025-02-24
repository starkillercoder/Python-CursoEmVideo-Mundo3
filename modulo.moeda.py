def metade(n=0, p=False):
    if p:
        return moeda(n / 2)
    else:
        return n / 2


def dobro(n=0, p=False):
    if p:
        return moeda(n*2)
    else:
        return n*2


def aumento(n=0, t=0, p=False):
    if p:
        return moeda(n * ((100 + t) / 100))
    else:
        return n * ((100 + t) / 100)


def reduz(n=0, t=0, p=False):
    if p:
        return moeda(n * ((100 - t)/100))
    else:
        return n * ((100 - t)/100)


def moeda(n, moeda='R$'):
    return f'{moeda}{n:.2f}'.replace('.',',')


def resumo(n=0, a=0, r=0):
    print('-' * 30)
    print(f'{'RESUMO DO VALOR':^30}')
    print('-' * 30)
    print(f'Preço analisado: \t{moeda(n)}')
    print(f'Dobro do preço: \t{dobro(n, True)}')
    print(f'Metade do preço: \t{metade(n, True)}')
    print(f'Aumentando {a}%: \t{aumento(n, a, True)}')
    print(f'Reduzindo {r}%: \t\t{reduz(n, r, True)}')
    print('-' * 30)
