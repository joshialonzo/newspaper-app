# built-in django modules
from django import forms

# custom django modules
from .models import New


class NewForm(forms.ModelForm):
    content = forms.CharField(
        label='',
        widget=forms.Textarea(
            attrs={
                'rows': 2,
                'placeholder': 'Redacte aquí la noticia'
            }),
        required=True)

    class Meta:
        model = New
        fields = ['content']
