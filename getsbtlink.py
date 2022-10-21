# Script python 3 para pegar link do video do SBT Videos

import requests
from bs4 import BeautifulSoup
import re

url = input('Link do Video do SBT Videos: ')
pagina_de_busca5 = requests.get(url)
soup5 = BeautifulSoup(pagina_de_busca5.text, "html.parser")
page5 = str(soup5)
thumb = str(soup5.find_all('div',attrs={'height':''}))
print(thumb[203:260].replace('https://player.sbtvideos.com.br/watch?videoId=','https://www.youtube.com/watch?v='))
