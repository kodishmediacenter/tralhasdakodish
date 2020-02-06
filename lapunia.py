# -*- coding: cp1252 -*-
import requests
from bs4 import BeautifulSoup
import re
import base64

def tmdb(ids):
    url = "https://www.themoviedb.org/movie/"+ids+"?language=pt-BR"
    pagina_de_busca = requests.get(url)
    soup = BeautifulSoup(pagina_de_busca.text, "html.parser")
    sintmdb = str(soup.find_all('meta',attrs={'property':'og:description'}))
    sintb = sintmdb.replace('[<meta content="','').replace('" property="og:description"/>]','')
    return sintb

def main():
    i = 0
    j = 0
    w = 0
    y = 0
    z = 0

    link = input('Digite o Link: ')
    fanart = input('Digite a fanart: ')
    #tmdbs = input('Digite codigo TMDB: ')
    
    pagina_de_busca = requests.get(link)
    soup = BeautifulSoup(pagina_de_busca.text, "html.parser")
    page = str(soup)
    nome = soup.find_all('title')
    
    nomes = str(nome)

    sin2 = re.search('SINOPSE(.*)',page).group(0)
    sin3 = str(sin2)
    sin4 = re.sub('</p>(.*)',r'',sin3).replace('SINOPSE</span>: </strong>','')
    sinopse = sin4
    qualidades = soup.find_all('',attrs={'':''})
    trailer = re.search('https://www.youtube.com/embed/(.*)?amp;showinfo=0&amp;theme=light&amp;autohide=0"',page).group(0)
    photo = re.search('https://image.tmdb.org(.*)',page).group(0)
    photo3 = re.sub('style="(.*)',r'',photo)
    photo2 = photo3.replace('" ','')
    
    magnet = re.search('magnet:(.*)',page)

    print(nomes.replace('[<meta content="','').replace('" property="og:title"/>]',''))
    titulo = nomes.replace('[<title> ','').replace(' Download</title>]','').replace('</title>]','')
    
    print(sin4)
    
    magnet1 = magnet.group(0).replace('magnet','\nmagnet').replace('"><img class="aligncenter" height="80" src="/720p.png" width="320"/></a><br/> <a href="','</link>').replace('"><img class="aligncenter" height="80" src="/1080p.png" width="320"/></a><br/> <a href="https://stfly.io/pCqifvDo" ','</link>')
    
    magnetx = '<item>\n<title>'+titulo+'</title>\n'
    
    magnet2 = re.sub('rel=(.*)',r'',magnet1).replace('announce"','announce</link>\n<thumbnail>'+photo2+'</thumbnail>\n<fanart></fanart>\n<info>'+sin4+'</info>\n</item>\n').replace('rarbg.to','rarbg.to</link>\n<thumbnail>'+photo2+'</thumbnail>\n<fanart>'+fanart+'</fanart>\n<info>'+sinopse+'</info>\n</item>\n').replace('magnet','\n <item>\n<title>'+titulo+'</title>\n<link>magnet')

    

    qualidades2 = str(qualidades)

    file = open("log.txt","a", encoding="utf-8") 
    file.write("") 
    print("<channels></channels>")
    file.write("<channels></channels>\n") 
    print("<channel>")
    file.write("<channel>\n")
    print("<name>"+titulo+"</name>")
    file.write("<name>"+titulo+"</name>\n")
    print("<thumbnail>"+photo2+"</thumbnail>")
    file.write("<thumbnail>"+photo2+"</thumbnail>\n")
    print(qualidades2.replace('[<span class="botao_dublado">','').replace('</span>,','').replace('<span class="botao_dublado">','\n').replace('</span>]',''))
    file.write(qualidades2.replace('[<span class="botao_dublado">','').replace('</span>,','').replace('<span class="botao_dublado">','\n').replace('</span>]',''))  
    file.write("")
    print(magnet2)
    file.write(magnet2)
    trailer2 = str(trailer)
    trailer3 = trailer2.replace('[<iframe allowfullscreen="" class="embed-responsive-item" src="','')
    trailer4 = re.sub('" title="Download (.*)"></iframe>]',r'',trailer3).replace('?amp;showinfo=0&amp;theme=light&amp;autohide=0"','')
    #print(trailer4)

    print("\n<item>")
    print("<title>Trailer</title>")
    print("<utube>"+trailer4.replace('https://www.youtube.com/embed/','')+"</utube>")
    print("<thumbnail>"+photo2+"</thumbnail>")
    print("<fanart></fanart>")
    print("<info></info>")
    print("</item>")
    print("</channel>")
    file.write("")
    file.write("<item>\n")
    file.write("<title>Trailer</title>\n")
    file.write("<utube>"+trailer4.replace('https://www.youtube.com/embed/','')+"</utube>\n")
    file.write("<thumbnail>"+photo2+"</thumbnail>")
    file.write("<fanart></fanart>\n")
    file.write("<info></info>\n")
    file.write("</item>\n")
    file.write("</channel>\n")  
    

    



    
main()
