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


class NotaForm(forms.ModelForm):
    class Meta:
        model = Nota
        fields = ["name", "desc"]
        widgets = {
            'desc': forms.Textarea()
        }

def clean(self, *args, **kwargs):
    cleaned_data = super(NotaForm, self).clean(*args, **kwargs)
