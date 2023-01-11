from django import forms
from .models import Carrito_Items

class Editar_Carrito_Form(forms.ModelForm):

    class Meta:
        model = Carrito_Items
        fields = ('cantidad', 'carrito')