import requests
from bs4 import BeautifulSoup
import re
import base64

link ='https://nyaa.si/?p=1'
headers = {'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'}
pagina_de_busca = requests.get(link,headers=headers)
soup = BeautifulSoup(pagina_de_busca.text, "html.parser")
page = str(soup)

#<tr class="default">


data = str(soup.find_all('tr', attrs={'class':'default'}))

data1 = re.sub('magnet','\nmagnet',data)
data2 = re.sub('<td class="text-center">(.*)</td>','',data1).replace('</td>','<td>')
data3 = re.sub('(.*)title="','',data2).replace('<a href="/download','https://nyaa.si/download').replace('<tr class="default">','').replace('<td>','').replace('<a href="','')
data4 = data3.replace('<td colspan="2">','').replace('<td class="text-center">','').replace('"><i class="fa fa-fw fa-','').replace('magnet"></i></a>','').replace('Literature - English-translated">','').replace('<img alt="Literature - English-translated" class="category-icon" src="/static/img/icons/nyaa/3_1.png"/>','')
data5 = data4.replace('</a>','')
data6 = re.sub('<td class="text-center" data-timestamp="(.*)">(.*)',r'',data5).replace('\n','').replace('</tr>,','\n\n').replace('download"></i>','\n').replace('https','\nhttps')
data7 = data6.replace('<img alt="Literature - Raw" class="category-icon" src="/static/img/icons/nyaa/3_3.png"/>','')
data8 = re.sub('(.*)">',r'',data7).replace('</tr>]','').replace('https','</title>\n<link>https').replace('torrent','torrent$nome=[B]Link .Torrent[/B]</link>').replace('magnet','<link>magnet').replace('announce\n','announce$nome=[B]Link Magnetico[/B]</link>\n<thumbnail>https://image.tmdb.org/t/p/w342/lUjQBUaYvduXcAfXjR5LrRdNFDY.jpg</thumbnail><fanart></fanart>\n<info></info>\n</item>\n')


print(data8)
#print(data3)
