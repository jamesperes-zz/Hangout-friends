
from urllib.request import urlopen
# trazer a página inteira
html = urlopen("http://www.globo.com/")
html_aberto = html.read()
print(html_aberto)
