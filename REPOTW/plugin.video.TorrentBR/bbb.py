import xbmc
import xbmcgui

def web_browser(urlcn):
        import webbrowser
        if xbmc . getCondVisibility ( 'system.platform.android' ) :
                ost = xbmc . executebuiltin ( 'StartAndroidActivity(,android.intent.action.VIEW,,%s)' % ( ''+urlcn+'' ) )
        else:
                ost = webbrowser . open ( ''+urlcn+'' )







def conect():
    url = "https://bbb.fm/"
    web_browser(url)



