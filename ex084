pessoa_peso = []
copia = []
cont_pessoas = 0
pesos = []
pessoas_pesada = []
pessoas_leves = []
while True:
    copia.append(str(input('Digite seu nome: ')))
    cont_pessoas += 1
    copia.append(int(input('Digite seu peso: ')))
    pessoa_peso.append(copia[:])
    copia.clear()
    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Deseja continuar? ')).upper().strip()[0]
    if resposta == 'N':
        break
for p in pessoa_peso:
    pesos.append(p[1])
for p in pessoa_peso:
    if p[1] == max(pesos):
        pessoas_pesada.append(p[0])
    if p[1] == min(pesos):
        pessoas_leves.append(p[0])
print(f'Foram cadastradas {cont_pessoas}.')
print(f'O maior peso foi {max(pesos)}. {pessoas_pesada}')
print(f'O menor peso foi {min(pesos)}. {pessoas_leves}')
