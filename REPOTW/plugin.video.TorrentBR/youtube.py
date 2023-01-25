

def addDir(title, url):
    liz=xbmcgui.ListItem(title)
    liz.setProperty('IsPlayable', 'false')
    liz.setInfo(type="Video", infoLabels={"label":title,"title":title} )
    liz.setArt({'thumb':ICON,'fanart':FANART})
    xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=url,listitem=liz,isFolder=True)


def youtube(url)
    addDir(title="Kodish Player", url="plugin://plugin.video.youtube/"+url+"/")
    xbmcplugin.endOfDirectory(int(sys.argv[1]),cacheToDisc=True)
