import grok
import zope.interface
import zeam.form.ztk.widgets.collection
import zeam.form.ztk.widgets.choice
from .skin import ISiguvTheme


grok.templatedir("templates")


class MultiChoiceFieldWidget(
        zeam.form.ztk.widgets.collection.MultiChoiceFieldWidget):
    grok.adapts(
        zeam.form.ztk.widgets.collection.SetField,
        zeam.form.ztk.widgets.collection.ChoiceField,
        zope.interface.Interface,
        ISiguvTheme)

    def htmlClass(self):
        return "form-check-input"


class RadioFieldWidget(zeam.form.ztk.widgets.choice.RadioFieldWidget):
    grok.adapts(
        zeam.form.ztk.widgets.choice.ChoiceField,
        zope.interface.Interface,
        ISiguvTheme)
    grok.name('radio')

    def myHtmlClass(self):
        return "form-check-input"

