aluno_nota = dict()
aluno_nota['nome'] = str(input('Nome do aluno: '))
aluno_nota['nota'] = float(input(f'Média de {aluno_nota['nome']}: '))
if aluno_nota['nota'] >= 7:
    aluno_nota['situacao'] = 'APROVADO'
else:
    aluno_nota['situacao'] = 'REPROVADO'
print()
print(f'O nome é igual a {aluno_nota['nome']}.')
print(f'A média é igual a {aluno_nota['nota']}.')
print(f'A situação é {aluno_nota['situacao']}.')
