jogo = dict()
gols = []
jogo['Nome'] = str(input('Nome do jogador: '))
jogos = int(input(f'Quantos jogos {jogo['Nome']} jogou? '))
for c in range(1, jogos + 1):
    gol = int(input(f'Quantos gols na partida {c}? '))
    gols.append(gol)
jogo['Gols'] = gols
jogo['Total'] = sum(jogo['Gols'])
print('-=' * 30)
for v, i in jogo.items():
    print(f'{v}: {i}')
print('-=' * 30)
print(f'O jogador {jogo['Nome']} jogou {jogos} partidas.')
for c, k in enumerate(jogo['Gols']):
    print(f' > Na partida {c + 1}, fez {k} gols.')
print(f'Foi um total de {jogo['Total']} gols.')
