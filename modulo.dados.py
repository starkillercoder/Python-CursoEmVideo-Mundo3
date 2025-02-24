def leiadinheiro(s):
    val = False
    while val == False:
        k = str(input(s)).replace(',', '.').strip()
        if k.isalpha() or k == '':
            print(f'{'\33[31m'}ERRO: "{k}" é um preço inválido!{'\33[m'}')
        else:
            val = True
            return float(k)
