# -*- coding: cp1252 -*-
import requests
from bs4 import BeautifulSoup
import re
import base64


def main(link,descricao):
    i = 0
    j = 0
    w = 0
    y = 0
    z = 0

    

    #link = "https://wolverdonfilme.net/alerta-maximo-torrent-2023-dual-audio-dublado-web-dl-1080p-4k-WF/"
    #photo = 'teste'
    headers = {'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'}
    pagina_de_busca = requests.get(link,headers=headers)
    soup = BeautifulSoup(pagina_de_busca.text, "html.parser")
    page = str(soup)

    nome = str(soup.find_all('meta', attrs={'name':'description'}))
    nome2 = nome.replace('[<meta content="Baixar Torrent','')
    nome3 = re.sub('Torrent .*',r'',nome2)
    magnet = str(soup.find_all('a'))
    magnet2 = re.search('magnet(.*)',magnet).group(0)
    magnet3 = re.sub('<img alt="MAGNET LINK" class="alignnone" decoding="async" height="(.*)" loading="lazy" src="(.*)" width="(.*)"/></noscript></a>',r'',magnet2)
    magnet4 = re.sub('<img .*','',magnet3)
    magnet5 = re.sub('">','',magnet4)

    img = str(soup.find_all('meta', attrs={'property':"og:image:secure_url"})).replace('[<meta content="','').replace('" property="og:image:secure_url"/>]','').replace('i1.wp.com/','')
    print('<item>')
    print('<title>'+nome3+'</title>')
    print('<link>'+magnet5+'$nome=[B]OP1 1080p[/B]</link>')
    trailer = str(soup.find_all('div', attrs={'class':"rll-youtube-player"})).replace('[<div class="rll-youtube-player" data-id="i9-t8H_5W0k" data-query="" data-src="','').replace('"></div>]','')
    trailer2 = trailer.replace('https://www.youtube.com/embed/','plugin://plugin.video.youtube/play/?video_id=')
    trailer3 = re.sub('.*plugin',r'plugin',trailer2)
    print('<link>plugin://'+trailer3+'$nome=[B]Trailer[/B]</link>')
    print('<thumbnail>'+img+'</thumbnail>')
    print('<fanart></fanart>\n<info>'+descricao+'</info>\n</item>\n')

    



    
#main()
