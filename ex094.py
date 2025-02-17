lista = list()
ficha = dict()
soma = 0
while True:
    ficha['nome'] = str(input('Nome: '))
    ficha['sexo'] = str(input('Sexo: [F/M] ')).upper()
    while ficha['sexo'] not in 'MF':
        print('ERRO! Digite somente F ou M!')
        ficha['sexo'] = str(input('Sexo: [F/M] ')).upper()
    ficha['idade'] = int(input('Idade: '))
    soma += ficha['idade']
    lista.append(ficha.copy())
    ficha.clear()
    resposta = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    while resposta not in 'SN':
        print('ERRO! Digite somente S ou N!')
        resposta = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    if resposta == 'N':
        break
print('-=' * 30)
print(f'O grupo tem {len(lista)} pessoas.')
print(f'A média de idade é de {soma/len(lista):.2f}')
print('As mulheres cadastradas foram: ', end=' ')
for c in lista:
    if c['sexo'] == 'F':
        print(c['nome'], end=' ')
print()
print('Lista das pessoas com idade acima da média: ')
for c in lista:
    if c['idade'] >= soma / len(lista):
        for k, v in c.items():
            print(f'{k} = {v};', end=' ')
        print()
print(f'{'ENCERRADO':=^60}')
