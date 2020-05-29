# -*- coding: cp1252 -*-
# -*- coding: utf-8 -*-


import requests
from bs4 import BeautifulSoup
import re

def cata_data(ids2,temp):

    headers2 = {'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'}
    url2 = "https://www.themoviedb.org/tv/"+ids2+"/season/"+temp+"?language=pt-BR"
    print(url2)
    pagina_de_busca3 = requests.get(url2,headers=headers2)
    soup2 = BeautifulSoup(pagina_de_busca3.text, "html.parser")
    page2 = str(soup2)

    #data = re.search('<p>(.*)</p>',page2)

    sin = soup2.find_all('div', attrs={'class': 'overview'})
    icones = soup2.find_all('img', attrs={'class': 'backdrop lazyload'})
    icones2 = str(icones)
    
    for data in sin:
        data1 = str(data)
        data2 = re.sub('</p>(.*)','',data1)
        data3 = re.sub('<div class="overview">',r'',data2)
        data4 = re.sub('</div>',r'',data3)
        data5 = re.sub('<p>',r'',data4)

        title = re.search('title="(.*)"',data1).group(0)
        title2 = re.sub('title="',r'<title>',title)
        title3 = re.sub('"',r'</title>',title2)
        icones3 = str(re.sub('(.*)data-src=',r'',icones2))
        icones4 = re.sub('data-srcset(.*)',r'',icones3)

        print('\n')
        print('<item>')
        print(title3)
        print('<link>--</link>')
        print('<link>--</link>')
        print('<thumbnail>'+icones4.replace('"','')+'</thumbnail>')
        print('<fanart></fanart>')
        print("<info>"+data5+"</info>")
        print('</item>')
        print('</channel>')

        
def main():
    temp0 = input('Tem a temporada Zero 1 (Sim) e 2 (Nao): ')
    ids2  = input('Digite o Codigo TMDB da Serie: ')
    qtemps  = int(input('Digite a quantidade de Temporadas: '))

    if temp0 == '1':
        qtemps2 = qtemps + 1
    else :
        qtemps2 = qtemps

    for j in range(qtemps2):
        if temp0 == '2':
            j1 = str(j+1)
            cata_data(ids2,j1)
        else:
            j1 = str(j)
            cata_data(ids2,j1)
            
        



#temp = "2"
#ids2 = "60735"

