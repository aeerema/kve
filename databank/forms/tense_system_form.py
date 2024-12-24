from django import forms 

from databank.models.language import Language
from databank.forms.widgets import intable_select_widget


class TenseSystemForm(forms.ModelForm):
    class Meta:
        model = Language
        fields = ['tense_system']
        labels = {'tense_system': ''}
        widgets = {'tense_system': intable_select_widget}
