# Python 3 code
import urllib.request, urllib.parse, urllib.error
import zipfile
import os,xbmcvfs,shutil,xbmcplugin,xbmcgui,xbmcaddon,xbmc
import sys
import re
import base64


ADDON_ID      = 'plugin.video.torrentbr'
REAL_SETTINGS = xbmcaddon.Addon(id=ADDON_ID)
ADDON_NAME    = REAL_SETTINGS.getAddonInfo('name')
ICON          = REAL_SETTINGS.getAddonInfo('icon')
FANART        = REAL_SETTINGS.getAddonInfo('fanart')


def setup_remote(nome):

    param2 = nome

    urll = re.sub('@(.*)',r'',param2)
    nomeD = re.sub('(.*)@',r'',param2)

    
    zip_file = "special://home/media/"
    api_file  = os.path.join(xbmcvfs.translatePath(zip_file))
    filezip = re.sub('plugin://kodish.repo.store/', r'', param2)
    filezip2 = str(filezip.replace("?file=",""))
    tam = len(filezip2)
    filezip21 = nomeD
    url = urll
    filezip2 = nomeD
    print("baixando addon ....")
    os.chdir (api_file) 
    urllib.request.urlretrieve(url, ""+filezip2+"")
    exemploZIP = zipfile.ZipFile (""+filezip2+"")
    exemploZIP.extractall()
    exemploZIP.close()
    source = ""+api_file+"/"+filezip21+""
    destination = "special://home/addons"
    destination2 = os.path.join(xbmcvfs.translatePath(destination))
    shutil.move(source, destination2)
    dialog = xbmcgui.Dialog()
    dialog.ok('Kodish Store', 'Addon Instalado com sucesso !!!')
    database.insert_id(filezip21)
