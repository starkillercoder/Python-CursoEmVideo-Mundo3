from modulos import moeda
p = float(input('Digite o preço: '))
print(f'A metade de {moeda.moeda(p)} é {moeda.metade(p, True)}')
print(f'O dobro de {moeda.moeda(p)} é {moeda.dobro(p, True)}')
print(f'Aumentando 10%, temos {moeda.aumento(p, 10, True)}')
print(f'Diminuindo 13%, temos {moeda.reduz(p, 13, True)}')
