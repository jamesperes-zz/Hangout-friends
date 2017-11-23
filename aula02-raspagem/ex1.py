
from urllib.request import urlopen
# trazer a página inteira
html = urlopen("http://www.globo.com/")
print(html.read())
