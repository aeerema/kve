from django import forms 

from databank.models.language import Language
from databank.forms.widgets import intable_select_widget


class FutForm(forms.ModelForm):
    class Meta:
        model = Language
        fields = ['fut']
        labels = {'fut': ''}
        widgets = {'fut': intable_select_widget}

        
class PstForm(forms.ModelForm):
    class Meta:
        model = Language
        fields = ['pst']
        labels = {'pst': ''}
        widgets = {'pst': intable_select_widget}