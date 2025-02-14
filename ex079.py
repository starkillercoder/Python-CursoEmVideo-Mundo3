numeros = []
while True:
    numero = int(input('Digite um número: '))
    if numero not in numeros:
        numeros.append(numero)
        print('Número adicionado com sucesso...')
    else:
        print('Número já adicionado...')
    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if resposta == 'N':
        break
print(sorted(numeros))
