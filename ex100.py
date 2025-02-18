from random import randint
lista = []
def sorteio():
    for c in range(1, 6):
        lista.append(randint(0, 10))
    print(f'Os números sorteados foram {lista}')
sorteio()
def somapar():
    pos = 0
    soma = 0
    while pos < 5:
        if lista[pos] % 2 == 0:
            soma += lista[pos]
        pos += 1
    print(f'A soma dos valores pares de {lista} é {soma}')
somapar()
