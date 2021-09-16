#https://jovemnerd.com.br/feed-nerdcast/

# -*- coding: cp1252 -*-

import requests
from bs4 import BeautifulSoup
import re

site = "http://feeds.feedburner.com/tkbrtokucast"
pagina_de_busca = requests.get(site)
soup = BeautifulSoup(pagina_de_busca.text, "html.parser")

i = 0

for titulo in soup.find_all('title'):
    data = str(titulo)
    data2 = data.replace('<title>','').replace('</title>','')
    i = i + 1
    if i > 2:
        arq = open("titulos.txt", 'a')
        arq.write(data2)
        arq.write("\n")
        arq.close()
    

for mp3 in soup.find_all('enclosure'):
    dmp3 = str(mp3)
    d2mp3 = re.sub('<enclosure length="(.*)" type="audio/mpeg" url="',r'',dmp3).replace('"></enclosure>','')
    arq = open("links.txt", 'a')
    arq.write(d2mp3)
    arq.write("\n")
    arq.close()
    #print(d2mp3)


linkss = open("links.txt", 'r')
tituloss = open("titulos.txt", 'r')

t2 = (linkss.readlines())
t3 = (tituloss.readlines())
t2s = len(t2)
t3s = len(t3)

podcast = open("servers.txt", 'a')
podcast.write("#EXTM3U")
podcast.write("\n")
podcast.close()

for t in range(0,t2s):
    podcast = open("servers.m3u", 'a')
    podcast.write('#EXTINF:-1 tvg-id="" tvg-logo="",'+t3[t]+'')
    podcast.write(t2[t])
    podcast.close()
    
