# -*- coding: utf-8 -*-
# Copyright (c) 2007-2011 NovaReto GMBH
# ck@novareto.de

import grok


from grokcore import layout
from zope.container.interfaces import IContainer
from zope.interface import Interface
from zope.traversing.browser import absoluteURL
from .resources import main_css, main_js


grok.templatedir('templates')


class ISiguvThemeLayer(grok.IDefaultBrowserLayer):
    pass


class ISiguvTheme(ISiguvThemeLayer):
    grok.skin('siguvtheme')


class Layout(layout.Layout):
    grok.context(Interface)
    grok.layer(ISiguvTheme)
    grok.name('uvc.siguvtheme')

    def update(self):
        main_css.need()
        main_js.need()

        site = grok.getSite()
        self.base = absoluteURL(site, self.request)
        if IContainer.providedBy(self.context) and self.base[:-1] != '/':
            self.base = self.base + '/'
