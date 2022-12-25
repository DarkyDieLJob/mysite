from django import forms
from .models import Proveedores

class Planilla_Form(forms.ModelForm):
    
    class Meta:
        model = Proveedores
        fields = [
            'nombre',
            'fecha',
            'archivo',
        ]
        fields = {
            'nombre':'nombre',
            'fecha':'fecha',
            'archivo':'archivo',
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class':'form.control'}),
            'fecha': forms.TextInput(attrs={'class':'form.control'}),
            'archivo': forms.ClearableFileInput,
        }