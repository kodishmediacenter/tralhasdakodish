# -*- coding: utf-8 -*-

import sys
import xbmcaddon, xbmcgui, xbmcplugin

# Plugin Info
ADDON_ID      = 'plugin.video.torrentbr'
REAL_SETTINGS = xbmcaddon.Addon(id=ADDON_ID)
ADDON_NAME    = REAL_SETTINGS.getAddonInfo('name')
ICON          = REAL_SETTINGS.getAddonInfo('icon')
FANART        = REAL_SETTINGS.getAddonInfo('fanart')

def addDir(title, url,icon):
    liz=xbmcgui.ListItem(title)
    liz.setProperty('IsPlayable', 'false')
    liz.setInfo(type="Video", infoLabels={"label":title,"title":title} )
    liz.setArt({'thumb':icon','fanart':FANART})
    xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=url,listitem=liz,isFolder=True)
    
def youtube(url-link):
    addDir(title="PLAY"            , url=""+url-link+"/",icon = "https://yt3.ggpht.com/ytc/AAUvwnjmc0Fn6LjfRcWF2BCgZwIHynmB2PK6DvhXjFstsA=s256-c-k-c0x00ffffff-no-rj-mo")
    xbmcplugin.endOfDirectory(int(sys.argv[1]),cacheToDisc=True)
