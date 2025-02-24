from modulos import moeda
p = float(input('Digite o preço: '))
print(f'A metade de {p} é {moeda.metade(p)}')
print(f'O dobro de {p} é {moeda.dobro(p)}')
print(f'Aumentando 10%, temos {moeda.aumento(p, 10):.2f}')
print(f'Diminuindo 13%, temos {moeda.reduz(p, 13):.2f}')
