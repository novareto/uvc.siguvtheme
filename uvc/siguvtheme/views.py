# -*- coding: utf-8 -*-
# # Copyright (c) 2007-2019 NovaReto GmbH
# # cklinger@novareto.de

import grok
import megrok.pagetemplate as pt
from zope.interface import Interface
from grokcore.chameleon.components import ChameleonPageTemplateFile

from zeam.form.base import Form
from .skin import ISiguvTheme


grok.templatedir("templates")


class FormMacros(grok.View):
    grok.context(Interface)
    grok.layer(ISiguvTheme)

    template = ChameleonPageTemplateFile("templates/formtemplate.cpt")


class FieldMacros(grok.View):
    grok.context(Interface)
    grok.layer(ISiguvTheme)

    template = ChameleonPageTemplateFile("templates/fieldtemplates.cpt")


class FormTemplate(pt.PageTemplate):
    grok.layer(ISiguvTheme)
    grok.view(Form)
