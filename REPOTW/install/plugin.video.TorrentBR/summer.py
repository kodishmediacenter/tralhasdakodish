# -*- coding: utf-8 -*- 
import sys 
import xbmcaddon, xbmcgui, xbmcplugin 
# Plugin Info

ADDON_ID      = 'plugin.video.torrentbr'
REAL_SETTINGS = xbmcaddon.Addon(id=ADDON_ID)
ADDON_NAME    = REAL_SETTINGS.getAddonInfo('name')
ICON          = REAL_SETTINGS.getAddonInfo('icon')
FANART        = REAL_SETTINGS.getAddonInfo('fanart')

YOUTUBE_CHANNEL_ID1 = "playlist/PLSUn1UQk9K4iRugrRwsSa8OKyIya-Qpwh"
YOUTUBE_CHANNEL_ID2 = "playlist/PL99Me1J57KdJqHbAGfzCxOdA4JOxGr0qP"
YOUTUBE_CHANNEL_ID3 = "playlist/PL99Me1J57KdJ9S_xf-Chb0xucJwiaHF0N"
YOUTUBE_CHANNEL_ID4 = "playlist/PLSUn1UQk9K4gpr_sO3kUGDXaXSt900wsU"

#icon1 = "https://liquipedia.net/commons/images/0/0c/Worlds_2021.png"
icon1 = "https://macmagazine.com.br/wp-content/uploads/2011/12/13-icone-app-summer-eletrohits.png"



def addDir(title, url, thumbnail):
    liz=xbmcgui.ListItem(title)
    liz.setProperty('IsPlayable', 'false')
    liz.setInfo(type="Video", infoLabels={"label":title,"title":title} )
    liz.setArt({'thumb':thumbnail,'fanart':FANART})
    xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=url,listitem=liz,isFolder=True)

def main():
   addDir(title = "Summer Eletrohits",url = "plugin://plugin.video.youtube/"+YOUTUBE_CHANNEL_ID1+"/",thumbnail = icon1,)
   addDir(title = "Summer Eletrohits 14",url = "plugin://plugin.video.youtube/"+YOUTUBE_CHANNEL_ID2+"/",thumbnail = icon1,)
   addDir(title = "Summer Eletrohits 15",url = "plugin://plugin.video.youtube/"+YOUTUBE_CHANNEL_ID3+"/",thumbnail = icon1,)
   addDir(title = "Summer Eletrohits 16",url = "plugin://plugin.video.youtube/"+YOUTUBE_CHANNEL_ID4+"/",thumbnail = icon1,)
   
   xbmcplugin.endOfDirectory(int(sys.argv[1]),cacheToDisc=True)


# summer.main()
