import grok
import uvcsite.browser.layout.menu

from .skin import ISiguvTheme
from zope import interface, component
from zope.viewlet.interfaces import IContentProvider


grok.templatedir("templates")


class Sidebar(uvcsite.browser.layout.menu.MenuRenderer):
    grok.context(interface.Interface)
    grok.layer(ISiguvTheme)

    bound_menus = ("quicklinks", "personalpreferences")
    
    def application_url(self):
        return grok.util.application_url(self.request, self.context)
