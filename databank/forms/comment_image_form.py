from django import forms 

from databank.models.comment_image import CommentImage
# from databank.forms.widgets import comment_widget


class CommentImageForm(forms.ModelForm):
    class Meta:
        model = CommentImage
        fields = ['image']
        labels = {'image': ''}
        # widgets = {'comment': comment_widget}