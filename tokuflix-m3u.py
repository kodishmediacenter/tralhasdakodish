nome = input('Digite o Nome do Seriado: ')
quant = int(input('Digite quantidade de Epsodios: '))
img = input('Digite link da imagem: ')
prefix = input('Digite Prefix: ')
sufix = input('Digite o sufixo: ')
zero = int(input('Incluir o Zero nos noves primeiros 1 - SIM  2 - NAO: '))
i = 0

files = open(""+nome+".m3u","a") 

files2 = open("gdatamx.xml","a") 
files2.write('')
files2.write(' <channels>\n')
files2.write(' <channel>\n')
files2.write(' <name>[COLOR white][B]'+nome+'[/B][/COLOR][COLOR cyan][B] ||| TOKUFLIX[/B][/COLOR][COLOR pink][B]NEO|||[/B][/COLOR]</name>\n')
files2.write(' <thumbnail>'+img+'</thumbnail>\n')
files2.write(' <externallink>base/'+nome+'.m3u</externallink>\n')
files2.write(' <fanart></fanart>\n')
files2.write(' <info></info>\n')
files2.write(' </channel>\n')
files2.write(' </channels>\n\n')
files2.close()

files.write('#EXTM3U\n')
files.close()

print('#EXTM3U')
for i in range(0,quant):
    i = i + 1
    ii = str(i)
    files = open(""+nome+".m3u","a") 
    files.write('#EXTINF:-1 tvg-id="" tvg-logo="'+img+'",'+nome+'- EP'+ii+'\n')
    #files.close()
    print('#EXTINF:-1 tvg-id="" tvg-logo="'+img+'",'+nome+'- EP'+ii+'')
    if zero == 1:
        if i < 10:
            print(''+prefix+'0'+ii+''+sufix+'')
            files.write(''+prefix+'0'+ii+''+sufix+'\b')
            files.close()
        else:
            print(''+prefix+''+ii+''+sufix+'')
            files.write(''+prefix+''+ii+''+sufix+'\n')
            files.close()
    else:
        print(''+prefix+''+ii+''+sufix+'')
        files.write(''+prefix+''+ii+''+sufix+'\n')
        files.close()
