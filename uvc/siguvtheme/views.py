# -*- coding: utf-8 -*-
# # Copyright (c) 2007-2019 NovaReto GmbH
# # cklinger@novareto.de

import grok
import uvcsite
import megrok.pagetemplate as pt


from .skin import ISiguvTheme
from zope.interface import Interface
from grokcore.chameleon.components import ChameleonPageTemplateFile


grok.templatedir("templates")


class FormMacros(grok.View):
    grok.context(Interface)
    template = ChameleonPageTemplateFile("templates/formtemplate.cpt")


class FieldMacros(grok.View):
    grok.context(Interface)
    template = ChameleonPageTemplateFile("templates/fieldtemplates.cpt")


class FormTemplate(pt.PageTemplate):
    grok.layer(ISiguvTheme)
    grok.view(uvcsite.browser.Form)
