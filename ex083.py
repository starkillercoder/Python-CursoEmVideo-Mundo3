cont = 0
parenteses = []
so_parenteses = []
expressao = str(input('Digite a expressão: '))
while True:
    if expressao[cont] in '()':
        parenteses.append(expressao[cont])
    cont += 1
    if cont == len(expressao):
        break
if parenteses.count('(') == parenteses.count(')') and ')' not in parenteses[:parenteses.count('(')]\
        and '(' not in parenteses[parenteses.count(')'):]:
    print('Equação pode ser resolvida.')
else:
    print('Equação não pode ser resolvida.')
