import grok
import zope.interface
import zeam.form.ztk.widgets.collection
from .skin import ISiguvThemeLayer


grok.templatedir("templates")


class MultiChoiceFieldWidget(
        zeam.form.ztk.widgets.collection.MultiChoiceFieldWidget):
    grok.adapts(
        zeam.form.ztk.widgets.collection.SetField,
        zeam.form.ztk.widgets.collection.ChoiceField,
        zope.interface.Interface,
        ISiguvThemeLayer)

    def htmlClass(self):
        return "form-check-input"
