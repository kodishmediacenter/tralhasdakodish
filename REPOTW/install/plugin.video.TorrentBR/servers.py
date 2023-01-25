import xbmc
import xbmcgui

def files(url):
    dialog = xbmcgui.Dialog()
    fn = dialog.browseSingle(1, 'Kodi', 'music', '', False, False, url)
    xbmc.Player().play(fn)


def menu():
    dialog = xbmcgui.Dialog()
    link = dialog.select('Servidores de Musica', ['Internacional (A-K)','Internacional (L-Z)','Internacional (server2)','Flashback','Metalica','Beatles (Server 01)','Beatles (Server 02)','Server 01','','','','','','','',''])

    if link == 0:
        url = "http://peterewendy.com.br/Genero/Mp3/INTERNACIONAL_(_A_-_K_)/"
        files(url)

    if link == 1:
        url = "http://peterewendy.com.br/Genero/Mp3/INTERNACIONAL_(_L_-_Z_)/"
        files(url)

    if link == 2:
        url = "https://teresadapraiamidis.com/Mp3/Musicas/Internacionais/"
        files(url)
        
    if link == 3:
        url = "http://peterewendy.com.br/Genero/Mp3/FLASHBACK/"
        files(url)

    if link == 4:
        url = "http://hcmaslov.d-real.sci-nnov.ru/public/mp3/Metallica/"
        files(url)

    if link == 5:
        url = "http://maslovd.ru/public/mp3/Beatles/"
        files(url)

    if link == 6:
        url = "http://hcmaslov.d-real.sci-nnov.ru/public/mp3/Beatles/"
        files(url)

    if link == 7:
        url = "http://aniz-music.com/Musicas/"
        files(url)

    if link == 8:
        url = ""
        files(url)
        
