# -*- coding: cp1252 -*-
# -*- coding: utf-8 -*-


import requests
from bs4 import BeautifulSoup
import re


    
    










    


link = input('Digite o ID da Serie: ')
#t5 = debrid_format(link)
ids2 = link



headers = {'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'}
url = "https://www.themoviedb.org/tv/"+ids2+"?language=pt-BR"

pagina_de_busca2 = requests.get(url,headers=headers)
soup = BeautifulSoup(pagina_de_busca2.text, "html.parser")
page = str(soup)

nome = soup.find_all('meta', attrs={'property': 'og:title'})
nome2 = str(nome)
sinopse = soup.find_all('meta', attrs={'property': 'og:description'})
sinopse2 =str(sinopse)
thumb = soup.find_all('meta', attrs={'property': 'og:image'})
thumb2 =str(thumb)


t1 = nome2.replace('[<meta content="','').replace('" property="og:title"/>]','')
t2 = sinopse2.replace('[<meta content="','').replace('" property="og:description"/>]','')
t3 = thumb2.replace('[<meta content="','').replace('" property="og:image"/>]','').replace('" property="og:image"/>, <meta content="','\n').replace('','')
t4 = re.sub('w780',r'original',t3)

print("====Cola isso menu principal ====\n\n")
print('<channels></channels>')
print('<channel>')
print('<name>'+t1+'</name>')
print('<thumbnail>'+t4+'</thumbnail>')

print("\n\n====Agora vou gerar parte dos sinopses e tudo em ordem ====\n\n")

import sinapse
sinapse.main()
