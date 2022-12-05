from django import forms

class Consultar_id(forms.Form):
    id = forms.CharField(label="Codigo del producto",max_length=20)