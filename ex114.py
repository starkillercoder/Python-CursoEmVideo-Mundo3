import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except:
    print('O site "Pudim" não está disponível!')
else:
    print('Consegui acessar o site "Pudim"!')
