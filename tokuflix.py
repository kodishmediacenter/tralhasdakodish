# Script Feito Por Kodish Media Center do Brasil
# 11 Fevereiro de 2020
# Script para pegar links do site cos.tv e fazer o Download


import requests
from bs4 import BeautifulSoup
import re



def pega_toku_mp4(url):
    headers = {'user-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/72.0'}
    pagina_de_busca3 = requests.get(url, headers=headers)
    soup3 = BeautifulSoup(pagina_de_busca3.text, "html.parser")
    page3 = str(soup3)

    link = str(soup3.find_all('meta',attrs={'itemprop':'contentUrl'}))
    print(link.replace('[<meta content="','').replace('" itemprop="contentUrl"/>]',''))

    
def pega_toku_sin(url):
    headers = {'user-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/72.0'}
    pagina_de_busca4 = requests.get(url, headers=headers)
    soup4 = BeautifulSoup(pagina_de_busca4.text, "html.parser")
    page4 = str(soup4)

    sin = str(re.search('title(.*)',page4).group(0))
    fsec = sin.replace('title>','').replace('- Tokuflix</title>','').replace('</','')
    print('#EXTINF:-1  group-title="Sem Categoria",'+fsec+'')

def pegar_toku_thumb(url):
    pagina_de_busca5 = requests.get(url)
    soup5 = BeautifulSoup(pagina_de_busca5.text, "html.parser")
    page5 = str(soup5)

    thumb = str(soup5.find_all('div',attrs={'class':'column'}))
    print(thumb)

    

# Funcao Principal 
def main():
    
    url = input('Digite o Link Tokuflix: ')
    #url = "https://www.tokuflix.com/2020/02/1966-ultra-q.html"

    conteudo = input('1 Filme e 2 Serie: ')
    cont = int(conteudo)

    if cont== 1: 
        pagina_de_busca2 = requests.get(url)
        soup2 = BeautifulSoup(pagina_de_busca2.text, "html.parser")
        page = str(soup2)
        titulo= re.search("(.*).html",page)
        #<h2 class='post-title entry-title'>
        thumb = str(soup2.find_all('a',attrs={'class':'playWrapper'}))
        thumb2 = re.search('href=(.*)',thumb).group(0)
        print(thumb2.replace('href="','').replace('">',''))
        murl = thumb2.replace('href="','').replace('">','')
        pega_toku_mp4(murl)
        pega_toku_sin(murl)
        pegar_toku_thumb(murl)
        
    if cont == 2:
        qdc = input('Quantidade de Eps: ')
        pref = input('Prefixo do Link: ')
        start = input('Quando vc deseja iniciar: ')
        qdc2 = int(qdc)
        start2 = int(start)
        for i in range(qdc2):
            i = i + start2
            ii = str(i)
            
            if i < 10:
                murl = ""+pref+"ep0"+ii+".html"
            else:
                murl = ""+pref+"ep"+ii+".html"
            pega_toku_sin(murl)
            pega_toku_mp4(murl)
            
            
        


    
        
        
        

main()
