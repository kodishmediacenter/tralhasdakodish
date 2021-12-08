import os
import wget
from PIL import Image

folder = input('Digite a Pasta do addon: ')
os.makedirs(folder)
nome = input('Digite o Nome do Addon: ')
desc = input('Descreva o que e o Addon: ')
versao = input('Versao do Addon: ')
desv = input('Qual desenvolvedor: ')
os.makedirs(""+folder+"/resources")
file = open("addon.xml","w") 
file.write('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n')
file.write('<addon id=\"'+folder+'\" name=\"'+nome+'\" version=\"'+versao+'\" provider-name=\"'+desv+'\">\n')
file.write('  <requires>\n')
file.write('    <import addon="xbmc.python2" version="3.0.0"/>\n')
file.write('    <import addon="plugin.video.youtube" version="5.0.0"/>\n')
file.write('  </requires>\n')
file.write(' <extension point="xbmc.python.pluginsource" library="default.py">\n')
file.write('    <provides>video</provides>\n')
file.write(' </extension>\n')
file.write(' <extension point="xbmc.addon.metadata">\n')
file.write('    <summary lang="en">'+nome+'</summary>\n')
file.write('    <description lang="en">'+desc+'</description>\n')
file.write('    <platform>all</platform>\n')
file.write('    <forum></forum>\n')
file.write('    <website></website>\n')
file.write('    <assets>\n')
file.write('    <icon>icon.jpg</icon>\n')
file.write('    </assets>\n')
file.write(' </extension>\n')
file.write('</addon>\n')
file.close()

file2 = open("default.py","w")
file2.write('# -*- coding: utf-8 -*- \n')

file2.write('import sys \n')
file2.write('import xbmcaddon, xbmcgui, xbmcplugin \n')
file2.write('import requests,json\n')

file2.write('# Plugin Info\n\n')
file2.write('ADDON_ID      = \''+folder+'\'\n')
file2.write('REAL_SETTINGS = xbmcaddon.Addon(id=ADDON_ID)\n')
file2.write('ADDON_NAME    = REAL_SETTINGS.getAddonInfo(\'name\')\n')
file2.write('ICON          = REAL_SETTINGS.getAddonInfo(\'icon\')\n')
file2.write('FANART        = REAL_SETTINGS.getAddonInfo(\'fanart\')\n\n')

canalytb = input('Digite o IP do servidor: ')

icone = "https://yt3.ggpht.com/ytc/AAUvwniHCQOcR1k6g5mIDH1C1YxU2pxsneZkOYKXEPVnlg=s256-c-k-c0x00ffffff-no-rj"
wget.download(icone)

#file2.write('YOUTUBE_CHANNEL_ID1=  \"'+canalytb+'\"\n')
#file2.write('icon1 = \"'+icone+'\"\n')

file2.write('lista = requests.get("'+canalytb+'").content\n')
file2.write('channellist = json.loads(lista)\n\n')
file2.write('def addDir(title, url, thumbnail):\n')
file2.write('    liz=xbmcgui.ListItem(title)\n')
file2.write('    liz.setProperty(\'IsPlayable\', \'false\')\n')
file2.write('    liz.setInfo(type="Video", infoLabels={"label":title,"title":title} )\n')
file2.write('    liz.setArt({\'thumb\':thumbnail,\'fanart\':FANART})\n')
file2.write('    xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=url,listitem=liz,isFolder=True)\n\n')


file2.write('if __name__ == \'__main__\':\n')
file2.write('   for name, id, icon in channellist:\n')
file2.write('      addDir(title = name,url = "plugin://plugin.video.youtube/"+id+"/",thumbnail = icon,)\n')
file2.write('   xbmcplugin.endOfDirectory(int(sys.argv[1]),cacheToDisc=True)\n')

file2.close()
os.rename("unnamed.jpg", "icon.jpg")

im1 = Image.open(r'icon.jpg')
im1.save(r'icon.png')

import shutil
shutil.copyfile('default.py',''+folder+'/default.py')
shutil.copyfile('addon.xml',''+folder+'/addon.xml')
shutil.copyfile('icon.jpg',''+folder+'/icon.jpg')
shutil.copyfile('icon.png',''+folder+'/icon.png')

fileup = open("logup.txt","a")
fileup.write('\n')
fileup.write('<td valign=\"top\"><img src=\"http://temporada.peraltas.com.br/wp-content/plugins/download-manager/assets/file-type-icons/download2.png\" height=\"20px\" width=\"20px\" alt=\"[   ]\"></td><td><a href=\"addons/'+folder+'.zip\">addons/'+folder+'.zip</a></td><td align=\"right\"> V:</td><td align=\"right\">'+versao+'</td></td></tr>')
fileup.close()
