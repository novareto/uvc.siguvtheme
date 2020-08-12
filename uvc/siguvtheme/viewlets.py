import grok
import uvc.menus.components
import uvc.menus.directives
#import uvcsite.browser.layout.slots

from .skin import ISiguvTheme
from zope import interface


grok.templatedir("templates")


class SiteCap(grok.ContentProvider):
    grok.context(interface.Interface)
    grok.layer(ISiguvTheme)
    grok.template("sitecap")


class PageHeader(grok.ContentProvider):
    grok.context(interface.Interface)
    grok.layer(ISiguvTheme)
    grok.template("header")


class GlobalMenu(uvc.menus.components.MenuRenderer):
    grok.context(interface.Interface)
    grok.layer(ISiguvTheme)

    bound_menus = ("globalmenu",)


#class GlobalMenuEntry(uvc.menus.components.MenuItem):
#    grok.layer(ISiguvTheme)
#    grok.order(20)
#    uvc.menus.directives.menu(
#        uvcsite.browser.layout.slots.interfaces.IGlobalMenu)
#
#    title = "Something"


#class GlobalMenuEntryActive(uvc.menus.components.MenuItem):
#    grok.layer(ISiguvTheme)
#    grok.order(10)
#    grok.name("index_page")
#    uvc.menus.directives.menu(
#        uvcsite.browser.layout.slots.interfaces.IGlobalMenu)
#
#    title = "Startseite"
#
#    def url(self):
#        return self.view.application_url()


class Sidebar(uvc.menus.components.MenuRenderer):
    grok.context(interface.Interface)
    grok.layer(ISiguvTheme)

    bound_menus = ("quicklinks", "personalpreferences")

    def application_url(self):
        return grok.util.application_url(self.request, self.context)

    def getPrincipalInformation(self):
        principal = self.request.principal
        ret = {}
        if principal.id == "zope.manager":
            ret["title"] = "ADMIN"
            ret["homefolder_url"] = "#"
        elif principal.id == "zope.anybody":
            ret["title"] = "ANON"
            ret["homefolder_url"] = "#"
        else:
            ret["title"] = principal.id
            ret["homefolder_url"] = principal.homefolder_url
        return ret


class Footer(grok.ViewletManager):
    grok.context(interface.Interface)
    grok.layer(ISiguvTheme)
