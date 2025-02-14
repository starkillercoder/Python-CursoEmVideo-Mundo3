from random import randint
from time import sleep
copia = []
palpites = []
cont = 0
jogos = int(input('Quantos jogos você quer que eu sorteie? '))
for cont in range(0, jogos):
    for c in range(0, 6):
        numero = randint(1, 60)
        while numero in palpites:
            numero = randint(1, 60)
        else:
            copia.append(numero)
        palpites.append(numero)
        copia.clear()
print(f'{f' Sorteando {jogos} jogos ':=^40}')
for c in range(0, jogos):
    print(f'{c + 1}º palpite: ', end=' ')
    if c == 0:
        print(sorted(palpites[0:6]))
    if c > 0:
        print(sorted(palpites[6 * c:6 * (c + 1)]))
    cont += 6
    sleep(0.5)
print(f'{' BOA SORTE ':=^40}')
