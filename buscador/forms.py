from django import forms

class Consultar_id(forms.Form):
    id = forms.CharField(label=    "Codigo del producto",max_length=20)
class Consultar_Barras(forms.Form):
    barras = forms.CharField(label="Codigo de barras___",max_length=13)
class Consultar_Nombre(forms.Form):
    nombre = forms.CharField(label="Nombre_____________",max_length=40)