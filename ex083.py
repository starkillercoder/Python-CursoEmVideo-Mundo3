pilha = []
expressao = str(input('Digite a expressão: '))
for c in expressao:
    if c == '(':
        pilha.append('(')
    if c == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
if len(pilha) == 0:
    print('Sua expressão está válida!')
else:
    print('Sua expressão está inválida!')
