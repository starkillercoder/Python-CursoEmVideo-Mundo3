gols = list()
ficha = list()
time = dict()
while True:
    total = 0
    time['nome'] = str(input('Nome do jogador: '))
    partida = int(input(f'Quantas partidas {time['nome']} jogou? '))
    for c in range(0, partida):
        gols.append(int(input(f'Quantos gols na partida {c + 1}? ')))
    time['gols'] = gols[:]
    time['total'] = sum(time['gols'])
    ficha.append(time.copy())
    gols.clear()
    time.clear()
    resposta = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    while resposta not in 'NS':
        print('ERRO! DIGITE S OU N')
    if resposta == 'N':
        break
print('=' * 49)
print(f'{'cod '}{'nome':<20}{'gols':<20}{'total':<5}')
print('-' * 49)
for i, c in enumerate(ficha):
    print(f'{i:<4}', end='')
    for d in c.values():
        print(f'{str(d):<20}', end='')
    print()
print('-' * 49)
while True:
    jogador = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if jogador == 999:
        break
    if 0 <= jogador < len(ficha):
        print(f'-- LEVANTAMENTO DO JOGADOR {ficha[jogador]['nome']}')
        for c, k in enumerate(ficha[jogador]['gols']):
            print(f'Jogo {c + 1}: {k} gols')
    elif jogador < 0 or jogador > len(ficha) - 1:
        print('JOGADOR NÃO EXISTE! TENTE NOVAMENTE!')
print(f'{' VOLTE SEMPRE ':=^49}')
