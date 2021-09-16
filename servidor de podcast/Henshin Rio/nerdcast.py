#https://jovemnerd.com.br/feed-nerdcast/

# -*- coding: cp1252 -*-

import requests
from bs4 import BeautifulSoup
import re

site = "https://anchor.fm/s/8665eec/podcast/rss"
pagina_de_busca = requests.get(site)
soup = BeautifulSoup(pagina_de_busca.text, "html.parser")

i = 0

for titulo in soup.find_all('title'):
    data = str(titulo)
    data2 = data.replace('<title>','').replace('</title>','').replace('<![CDATA[','').replace(']]>','').encode("utf-8")
    data3 = str(data2)
    i = i + 1
    if i > 2:
        arq = open("titulos.txt", 'a')
        arq.write(data3)
        arq.write("\n")
        arq.close()
    

for mp3 in soup.find_all('enclosure'):
    dmp3 = str(mp3)
    d2mp3 = re.sub('<enclosure length="(.*)" type="audio/mpeg" url="',r'',dmp3).replace('"></enclosure>','')
    d3mp3 = re.sub('" length="(.*)"',r'',d2mp3)
    arq = open("links.txt", 'a')
    arq.write(d3mp3)
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
    podcast.write('#EXTINF:-1 tvg-id="" tvg-logo="",'+t3[t].encode("utf-8")+'')
    podcast.write(t2[t])
    podcast.close()
    
