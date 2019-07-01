import grok
import uvcsite.browser.layout.menu

from .skin import ISiguvTheme
from zope import interface


grok.templatedir("templates")


class Sidebar(uvcsite.browser.layout.menu.MenuRenderer):
    grok.context(interface.Interface)
    grok.layer(ISiguvTheme)

    bound_menus = ("quicklinks", "personalpreferences")

    def application_url(self):
        return grok.util.application_url(self.request, self.context)


class Footer(grok.ViewletManager):
    grok.context(interface.Interface)
    grok.layer(ISiguvTheme)
