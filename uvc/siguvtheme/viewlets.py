# -*- coding: utf-8 -*-
# # Copyright (c) 2007-2019 NovaReto GmbH
# # cklinger@novareto.de


import grok

from .skin import ISiguvTheme
from zope import interface, component
from zope.viewlet.interfaces import IContentProvider


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
        if menu is not None:
            return menu.getMenuItems()
        return None

    @property
    def usermenu(self):
        menu = component.queryMultiAdapter(
            (self.view.context, self.request, self.view),
            IContentProvider,
            "personalpreferences",
        )
        if menu is not None:
            return menu.getMenuItems()
        return None


class Footer(grok.ViewletManager):
    grok.context(interface.Interface)
    grok.layer(ISiguvTheme)
