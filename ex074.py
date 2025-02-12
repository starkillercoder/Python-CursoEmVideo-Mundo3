from random import randint
numeros = (randint(0, 10), randint(0, 10), randint(0, 10),
           randint(0, 10), randint(0, 10))
print(numeros)
print(f'O maior valor é {max(numeros)}')
print(f'O menor valor é {min(numeros)}')
