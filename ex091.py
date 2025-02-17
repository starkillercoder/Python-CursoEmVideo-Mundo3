from random import randint
from time import sleep
from operator import itemgetter
jogo = {'jogador1': f'{randint(1, 6)}', 'jogador2': f'{randint(1, 6)}',
        'jogador3': f'{randint(1, 6)}', 'jogador4': f'{randint(1, 6)}'}
ranking = dict()
for j, d in jogo.items():
    print(f'{j}: {d} no dado.')
    sleep(1)
print()
print('-=' * 21)
print(f'{'Ranking':^21}')
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
for j, d in ranking:
    print(f' {j}: {d} no dado. ')
