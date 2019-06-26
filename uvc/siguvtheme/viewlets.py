# -*- coding: utf-8 -*-
# # Copyright (c) 2007-2019 NovaReto GmbH
# # cklinger@novareto.de


import grok

from .skin import ISiguvTheme
from zope import interface, component
from zope.viewlet.interfaces import IContentProvider
from uvcsite.browser.layout.menu import IMenu

grok.templatedir("templates")


class Sidebar(grok.ViewletManager):
    grok.context(interface.Interface)
    grok.layer(ISiguvTheme)

    def application_url(self):
        return grok.util.application_url(self.request, self.context)

    def quicklinks(self):
        menu = component.queryMultiAdapter(
            (self.view.context, self.request, self.view), IContentProvider, "quicklinks"
        )
        menu.update()
        return menu.viewlets

    def usermenu(self):
        menu = component.queryMultiAdapter(
            (self.view.context, self.request, self.view),
            IMenu,
            "personalpreferences",
        )
        if menu:
            import pdb; pdb.set_trace()
            return menu.entries()
        return []

    def update(self):
        print(self.usermenu())
        print(self.quicklinks())


class Footer(grok.ViewletManager):
    grok.context(interface.Interface)
    grok.layer(ISiguvTheme)
