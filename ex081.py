numeros = []
numeros_cont = 0
while True:
    numero = int(input('Digite um número: '))
    numeros.append(numero)
    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Deseja continuar? [S/N]: ')).upper().strip()[0]
    if resposta == 'N':
        break
print('-=' * 30)
print(f'Você digitou {len(numeros)} elementos.')
numeros.sort(reverse=True)
print(f'Os valores em ordem decrescente são {numeros}')
if 5 in numeros:
    print(f'O valor 5 está na lista.')
else:
    print(f'O valor 5 não está na lista.')
