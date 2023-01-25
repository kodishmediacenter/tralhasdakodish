# -*- coding: utf-8 -*- 
import sys 
import xbmcaddon, xbmcgui, xbmcplugin 
# Plugin Info

ADDON_ID      = 'plugin.video.hidratuxedo'
REAL_SETTINGS = xbmcaddon.Addon(id=ADDON_ID)
ADDON_NAME    = REAL_SETTINGS.getAddonInfo('name')
ICON          = REAL_SETTINGS.getAddonInfo('icon')
FANART        = REAL_SETTINGS.getAddonInfo('fanart')

YOUTUBE_CHANNEL_ID1 = "channel/UC48rkTlXjRd6pnqqBkdV0Mw/live"
YOUTUBE_CHANNEL_ID2 = "channel/UCSF_aFGIIIoWY30GVV19TKA/live"
YOUTUBE_CHANNEL_ID3 = "channel/UCKVlixycWmapnGQ_wht4cHQ/live"
YOUTUBE_CHANNEL_ID4 = "channel/UCZtmNrG53nmbq-Ww2VJrxEQ/live"
YOUTUBE_CHANNEL_ID5 = "channel/UCaFMdq6QrAAEx5k2cLlZNPA/live"

#icon1 = "https://liquipedia.net/commons/images/0/0c/Worlds_2021.png"
icon10 = "https://raw.githubusercontent.com/kodishmediacenter/Rework-hidra/main/icones/ddcw3vz-fbbdb42b-5378-4929-99c5-18deb56484c7.png"



def addDir(title, url, thumbnail):
    liz=xbmcgui.ListItem(title)
    liz.setProperty('IsPlayable', 'false')
    liz.setInfo(type="Video", infoLabels={"label":title,"title":title} )
    liz.setArt({'thumb':thumbnail,'fanart':FANART})
    xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=url,listitem=liz,isFolder=True)

def main():
   addDir(title = "Cblol 2022 1º Split (Brasil)",url = "plugin://plugin.video.youtube/"+YOUTUBE_CHANNEL_ID1+"/",thumbnail = icon10,)
   addDir(title = "LCS 2022 1º Split (EUA)",url = "plugin://plugin.video.youtube/"+YOUTUBE_CHANNEL_ID2+"/",thumbnail = icon10,)
   addDir(title = "LCK 2022 1º Split (Coreia)",url = "plugin://plugin.video.youtube/"+YOUTUBE_CHANNEL_ID3+"/",thumbnail = icon10,)
   addDir(title = "LEC 2022 1º Split (Europeu)",url = "plugin://plugin.video.youtube/"+YOUTUBE_CHANNEL_ID4+"/",thumbnail = icon10,)
   addDir(title = "LPL 2022 1º Split (China)",url = "plugin://plugin.video.youtube/"+YOUTUBE_CHANNEL_ID5+"/",thumbnail = icon10,)
   xbmcplugin.endOfDirectory(int(sys.argv[1]),cacheToDisc=True)
