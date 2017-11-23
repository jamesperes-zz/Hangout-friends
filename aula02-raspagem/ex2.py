from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen('http://www.globo.com')
bsObj = BeautifulSoup(html.read(), 'html.parser')


lista = bsObj.findAll('div')
for text in lista:
    pesquisa = str(text)
    print("*" * 100)
    if pesquisa.find("Anitta") == -1:
        print("No 'is' here!")
    else:
        print(text.getText())