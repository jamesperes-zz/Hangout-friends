import urllib.request
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen("http://sportv.globo.com/site/e-sportv/")
bsObj = BeautifulSoup(html, "html.parser")
images = bsObj.findAll("img", {"src":re.compile(".jpg")})


url = 'http://sportv.globo.com/site/e-sportv/'
for image in images:

    img = image["src"]
    name = img.split('/')[-1]
    print(name)
    print('*'* 100)
    urllib.request.urlretrieve(img, name)
