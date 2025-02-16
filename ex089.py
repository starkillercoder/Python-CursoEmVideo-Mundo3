sala = []
while True:
    nome = str(input('Nome: '))
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))
    media = (n1 + n2) / 2
    sala.append([nome, [n1, n2], media])
    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if resposta == 'N':
        break
print(f'{'No.':<4}{'Nome':<20}{'Média':>4}')
for i, v in enumerate(sala):
    print(f'{i:<4}{v[0]:<20}{v[2]:>4}')
while True:
    notas = int(input('Mostrar notas de qual aluno? (999 para para)'))
    if notas == 999:
        break
    if 0 <= notas <= len(sala) - 1:
        print(f'Notas de {sala[notas][0]}: {sala[notas][1]}')
