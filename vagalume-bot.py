#encoding: utf-8

import requests
from bs4 import BeautifulSoup
import re
import base64


def estacao(links):
    i = 0
    j = 0
    w = 0
    y = 0
    z = 0

    link = links

    
    headers = {'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'}
    pagina_de_busca = requests.get(link,headers=headers)
    soup = BeautifulSoup(pagina_de_busca.text, "html.parser")

    titulobr = str(soup.find_all('meta', attrs={'property':'og:title'})).replace('[<meta content="','').replace('" property="og:title"/>]','')
    metadato = str(soup.find_all('meta', attrs={'property':'og:image'}))
    metadato2 = metadato.replace('[<meta content="','').replace('" property="og:image"/>]','')

    img = metadato2
    linkm3u = img.replace('https://img.vagalume.fm/','https://stream.vagalume.fm/hls/').replace('/default','/index.m3u8').replace('/featured','/index.m3u8')
    print('<item>')
    print('<title>'+titulobr+'</title>')
    print('<link>'+linkm3u+'</link>')
    print('<thumbnail>'+img+'</thumbnail>')
    print('<fanart></fanart>\n<info></info>\n</item>\n')

    


def links():
    link = "https://vagalume.fm"
    headers = {'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'}
    pagina_de_busca = requests.get(link,headers=headers)
    soup = BeautifulSoup(pagina_de_busca.text, "html.parser")

    stations = (soup.find_all('li', attrs={'class':'station'}))
    
    for i in stations:
        stations21 = str(i)
        stations21 = re.sub('<li class="station" data-id="(.*)" data-name="(.*)" data-slug="(.*)" data-updated="(.*)">',r'',stations21)
        stations22 = re.sub('<picture>(.*)',r'',stations21).replace('</div>','').replace('</a>','').replace('</li>','')
        stations23 = re.sub('<img alt=(.*)',r'',stations22)
        stations24 = re.sub('<button class="(.*)" data-id="(.*)" data-plugin="play-button" data-slug="(.*)" data-type="tile"',r'',stations23)
        stations24 = re.sub('</button>',r'',stations24)
        stations24 = re.sub('</picture>',r'',stations24)
        stations24 = re.sub('<div class="desc">',r'',stations24)
        stations24 = re.sub('<span class="listeners"></span>',r'',stations24)
        stations24 = re.sub('</p>',r'',stations24)
        stations24 = re.sub('<p data-plugin="limit-desc">',r'',stations24)
        stations24 = re.sub('				',r'',stations24).replace('\n','')
        stations24 = re.sub('>>(.*)',r'',stations24).replace('<a href="/','https://vagalume.fm/')
        stations25 = re.sub('" title="(.*)"',r'',stations24)
        estacao(stations25)

    
    




links()

    
