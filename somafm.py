#encoding: utf-8

import requests
from bs4 import BeautifulSoup
import re
import base64



    
cont = 0

def links():
    link = "https://somafm.com/#alpha"
    headers = {'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'}
    pagina_de_busca = requests.get(link,headers=headers)
    soup = BeautifulSoup(pagina_de_busca.text, "html.parser")

    stations = (soup.find_all('li', attrs={'class':'cbshort'}))
    cont = 0
    
    for i in stations:
        cont = cont + 1
        #print(cont)
        stations21 = str(i)
        stations22 = stations21.replace('<a href="','https://somafm.com').replace('<li class="cbshort">','')
        stations23 = re.sub('">(.*)',r'',stations22)
        stations24 = re.sub('<img alt="(.*)" height="120" src="/',r'https://somafm.com/',stations23).replace('" width="120"/></a>','').replace('<h3>','').replace('</h3>','')
        stations25 = stations24.replace('<p class="descr','').replace('</li>','')
        stations26 = stations25.replace('https://somafm.com/','https://somafm.com/m3u/').replace('https://somafm.com/m3u/img','https://somafm.com/img')
        stations27 = re.sub('https://somafm.com/m3u/',r'',stations26)
        stations28 = re.sub('https(.*)',r'',stations27)
        stations29 = re.sub('/',r'.m3u',stations28).replace('\n','').replace('.m3u','-128-mp3$nome=[B]')
        stations30 = '<link>https://ice3.somafm.com/'+stations29+'[/B]</link>'
        print(stations30)

        if cont == 38:
            break

        


    
    




links()

    
