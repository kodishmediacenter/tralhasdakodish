# -*- coding: utf-8 -*- 
import sys 
import xbmcaddon, xbmcgui, xbmcplugin 
# Plugin Info

ADDON_ID      = 'plugin.video.torrentbr'
REAL_SETTINGS = xbmcaddon.Addon(id=ADDON_ID)
ADDON_NAME    = REAL_SETTINGS.getAddonInfo('name')
ICON          = REAL_SETTINGS.getAddonInfo('icon')
FANART        = REAL_SETTINGS.getAddonInfo('fanart')

YOUTUBE_CHANNEL_ID1 = "channel/UCSF_aFGIIIoWY30GVV19TKA/live"
YOUTUBE_CHANNEL_ID2 = "channel/UCKVlixycWmapnGQ_wht4cHQ/live"
YOUTUBE_CHANNEL_ID2 = "channel/UCZtmNrG53nmbq-Ww2VJrxEQ/live"
#icon1 = "https://liquipedia.net/commons/images/0/0c/Worlds_2021.png"
icon1 = "https://raw.githubusercontent.com/kodishmediacenter/Rework-hidra/main/icones/cblol.png"



def addDir(title, url, thumbnail):
    liz=xbmcgui.ListItem(title)
    liz.setProperty('IsPlayable', 'false')
    liz.setInfo(type="Video", infoLabels={"label":title,"title":title} )
    liz.setArt({'thumb':thumbnail,'fanart':FANART})
    xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=url,listitem=liz,isFolder=True)

def main():
   addDir(title = "LCS 2022 1º Split",url = "plugin://plugin.video.youtube/"+YOUTUBE_CHANNEL_ID1+"/",thumbnail = icon1,)
   addDir(title = "LCK 2022 1º Split",url = "plugin://plugin.video.youtube/"+YOUTUBE_CHANNEL_ID2+"/",thumbnail = icon2,)
   addDir(title = "LEC 2022 1º Split",url = "plugin://plugin.video.youtube/"+YOUTUBE_CHANNEL_ID3+"/",thumbnail = icon3,)
   xbmcplugin.endOfDirectory(int(sys.argv[1]),cacheToDisc=True)
