lista_compras = ('Macarrão', 10, 'Biscoito', 4)
cont_compras = 0
cont_precos = 1
print('-' * 35)
print(f'{'LISTAGEM DE PREÇOS':^35}')
print('-' * 35)
while True:
    print(lista_compras[cont_compras],end='')
    print('.' * (26 - len(lista_compras[cont_compras])), end='')
    print(f'R${lista_compras[cont_precos]:7.2f}')
    cont_compras += 2
    cont_precos += 2
    if cont_precos == len(lista_compras) + 1:
        break
print('-' * 35)
