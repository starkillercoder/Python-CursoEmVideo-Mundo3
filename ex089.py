notas = []
alunos = []
sala = (alunos, notas)
cont = 0
while True:
    nome = str(input('Nome do aluno: '))
    alunos.append(nome)
    nota1 = int(input('Nota 1: '))
    notas.append(nota1)
    nota2 = int(input('Nota 2: '))
    notas.append(nota2)
    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Deseja continuar? [S/N]: ')).upper().strip()[0]
    if resposta == 'N':
        break
print(f'{'No.':<3}', f'{'NOME':<20}', f'{'MÉDIA':<10}')
for c in range(0, len(alunos)):
    print(f'{c:<3}', f'{alunos[c]:<20}', f'{((notas[0 + cont] + notas[1 + cont]) / 2):<10}')
    cont += 1
while True:
    ver_notas = int(input('Mostrar notas de qual aluno? (999 para parar)'))
    while ver_notas < 0 or ver_notas > cont - 1:
        ver_notas = int(input('Mostrar notas de qual aluno? (999 para parar)'))
    if ver_notas == 999:
        break
    print(f'Notas de {alunos[ver_notas]} são: {notas[ver_notas], notas[ver_notas + 1]}')
