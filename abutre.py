# -*- coding: cp1252 -*-
import requests
from bs4 import BeautifulSoup
import re
import base64


def main():
    i = 0
    j = 0
    w = 0
    y = 0
    z = 0

    link = input('Digite o Link: ')
    photo = input('Digite a foto: ')
    pagina_de_busca = requests.get(link)
    soup = BeautifulSoup(pagina_de_busca.text, "html.parser")
    page = str(soup)
    nome = soup.find_all('meta', attrs={'property':'og:title'})
    sin = soup.find_all('div', attrs={'id':'sinopse'})
    nomes = str(nome)
    sin2 = str(sin)
    qualidades = soup.find_all('span',attrs={'class':'botao_dublado'})
    trailer = soup.find_all('iframe',attrs={'class':'embed-responsive-item'})
    photo2 = str(photo.replace('w185_and_h278_bestv2','w600_and_h900_bestv2').replace('w94_and_h141_bestv2','w600_and_h900_bestv2'))
    
    magnet = re.search('magnet:(.*)',page)

    print(nomes.replace('[<meta content="','').replace('" property="og:title"/>]',''))
    titulo = nomes.replace('[<meta content="','').replace('" property="og:title"/>]','')
    sint = len(sin2)
    print(sin2[31:sint].replace('<strong>','').replace('</strong>','').replace('<p>','').replace('</p>','').replace('</div>]',''))
    sinopse = sin2[31:sint].replace('<strong>','').replace('</strong>','').replace('<p>','').replace('</p>','').replace('</div>]','')
    magnet1 = magnet.group(0).replace('magnet','\nmagnet')
    magnetx = '<item>\n<title>'+titulo+'</title>\n'
    
    magnet2 = re.sub('rel=(.*)',r'',magnet1).replace('announce"','announce</link>\n<thumbnail>'+photo2+'</thumbnail>\n<fanart></fanart>\n<info>'+sinopse+'</info>\n</item>\n').replace('magnet','<item>\n<title>'+titulo+'</title>\n<link>magnet')

    

    qualidades2 = str(qualidades)

    file = open("log.txt","a") 
    file.write("") 
    print("<channels></channels>")
    file.write("<channels></channels>") 
    print("<channel>")
    file.write("<channel>")
    print("<name>"+titulo+"</name>")
    file.write("<name>"+titulo+"</name>")
    print("<thumbnail>"+photo2+"</thumbnail>")
    file.write("<thumbnail>"+photo2+"</thumbnail>")
    print(qualidades2.replace('[<span class="botao_dublado">','').replace('</span>,','').replace('<span class="botao_dublado">','\n').replace('</span>]',''))
    file.write(qualidades2.replace('[<span class="botao_dublado">','').replace('</span>,','').replace('<span class="botao_dublado">','\n').replace('</span>]',''))  
    print(magnet2)
    file.write(magnet2)
    trailer2 = str(trailer)
    trailer3 = trailer2.replace('[<iframe allowfullscreen="" class="embed-responsive-item" src="','')
    trailer4 = re.sub('" title="Download (.*)"></iframe>]',r'',trailer3)
    #print(trailer4)

    print("<item>")
    print("<title>Trailer</title>")
    print("<utube>"+trailer4.replace('https://www.youtube.com/embed/','')+"</utube>")
    print("<thumbnail>"+photo2+"</thumbnail>")
    print("<fanart></fanart>")
    print("<info></info>")
    print("</item>")
    print("</channel>")

    file.write("<item>")
    file.write("<title>Trailer</title>")
    file.write("<utube>"+trailer4.replace('https://www.youtube.com/embed/','')+"</utube>")
    file.write("<thumbnail>"+photo2+"</thumbnail>")
    file.write("<fanart></fanart>")
    file.write("<info></info>")
    file.write("</item>")
    file.write("</channel>")  
    

    



    
main()
