def area():
    medida = a * l
    print(f'Seu terreno tem medidas {a}x{l} e possui área de {medida}m².')


print(f'{' CONTROLE DE TERRENOS ':-^60}')
a = float(input('Largura do terreno (m): '))
l = float(input('Comprimento do terreno (m): '))
area()
print('-' * 60)
