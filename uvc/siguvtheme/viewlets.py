import grok
import uvcsite.browser.layout.menu
import uvcsite.browser.layout.slots

from .skin import ISiguvTheme
from zope import interface


grok.templatedir("templates")


class PageHeader(grok.ContentProvider):
    grok.context(interface.Interface)
    grok.layer(ISiguvTheme)
    grok.template('header')


class GlobalMenu(uvcsite.browser.layout.menu.MenuRenderer):
    grok.context(interface.Interface)
    grok.layer(ISiguvTheme)

    bound_menus = ("globalmenu", )


class GlobalMenuEntry(uvcsite.browser.layout.menu.MenuItem):
    grok.layer(ISiguvTheme)
    uvcsite.browser.layout.menu.menu(
        uvcsite.browser.layout.slots.interfaces.IGlobalMenu)
    grok.order(20)

    title = "Something"


class GlobalMenuEntryActive(uvcsite.browser.layout.menu.MenuItem):
    grok.layer(ISiguvTheme)
    uvcsite.browser.layout.menu.menu(
        uvcsite.browser.layout.slots.interfaces.IGlobalMenu)
    grok.order(10)
    grok.name('index_page')
    title = "Startseite"

    def url(self):
        return self.view.application_url()


class Sidebar(uvcsite.browser.layout.menu.MenuRenderer):
    grok.context(interface.Interface)
    grok.layer(ISiguvTheme)

    bound_menus = ("quicklinks", "personalpreferences")

    def application_url(self):
        return grok.util.application_url(self.request, self.context)


class Footer(grok.ViewletManager):
    grok.context(interface.Interface)
    grok.layer(ISiguvTheme)
