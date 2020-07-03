from django import forms
from .models import ComprarArticulo, Nota


class CompraModelForm(forms.ModelForm):
    class Meta:
        model = ComprarArticulo
        fields = ["nombre", "categoria", "descripcion"]
        widgets = {
            'descripcion': forms.Textarea()
        }


def clean(self, *args, **kwargs):
    cleaned_data = super(CompraModelForm, self).clean(*args, **kwargs)


class NotaForm(forms.Form):
    name = forms.CharField(max_length = 500)
    desc = forms.CharField(max_length= 500)        
