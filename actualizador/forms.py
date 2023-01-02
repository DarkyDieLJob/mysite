from django import forms
from .models import Proveedores

class CustomClearableFileInput(forms.ClearableFileInput):
    template_with_clear = '<br>  <label for="%(clear_checkbox_id)s">%(clear_checkbox_label)s</label> %(clear)s'
 
class Planilla_Form(forms.ModelForm):
    
    class Meta:
        model = Proveedores
        fields = [
            'nombre',
            'archivo',
        ]
        fields = {
            'nombre':'nombre',
            'archivo':'archivo',
        }
        

        def __init__(self, *args, **kwargs):
            self.fields['nombre'].widget = forms.Textarea(attrs={'class': 'md-textarea', 'style': 'height: 75px'})
        widgets = {
            'archivo': CustomClearableFileInput,
        }