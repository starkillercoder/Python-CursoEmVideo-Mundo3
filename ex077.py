lista_palavras = ('amar', 'jogar', 'sistemas')
palavras = letras = 0
while True:
    if letras == 0:
        print(f'\nA palavra {lista_palavras[palavras]} tem as vogais:', end=' ')
    if lista_palavras[palavras][letras].upper() in 'AEIOU':
        print(lista_palavras[palavras][letras], end=' ')
    letras += 1
    if letras == len(lista_palavras[palavras]):
        palavras += 1
        letras = 0
    if palavras == len(lista_palavras):
        break
