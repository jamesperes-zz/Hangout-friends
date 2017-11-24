from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen('http://www.globo.com')
bsObj = BeautifulSoup(html.read(), 'html.parser')


lista = bsObj.findAll('div')


for item in lista:

    item_str = str(item)

    if item_str.find('Fla') == -1:
        pass
    elif 'background-image' in item_str:
        pass
    else:
        print(item.getText())
        print("*" * 100)


