from django import forms
from .models import Proveedores

class CustomClearableFileInput(forms.ClearableFileInput):
    template_with_clear = '<br>  <label for="%(clear_checkbox_id)s">%(clear_checkbox_label)s</label> %(clear)s'
 
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
            'archivo': CustomClearableFileInput,
        }