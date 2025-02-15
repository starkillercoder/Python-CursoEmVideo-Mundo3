from random import randint
from time import sleep
copia = []
palpites = []
cont = 0
jogos = int(input('Quantos jogos você quer que eu sorteie? '))
for cont in range(0, jogos):
    for c in range(0,6):
        numero = randint(1, 60)
        while numero in copia:
            numero = randint(1, 60)
        copia.append(numero)
    palpites.append(copia[:])
    copia.clear()
print(f'{f' SORTEANDO {jogos} JOGOS ':=^40}')
for c in range(0, jogos):
    print(f'{c + 1}º jogo: {sorted(palpites[c])}')
    sleep(1)
print(f'{'BOA SORTE':=^40}')
