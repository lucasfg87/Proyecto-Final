from django import forms
from ejemplo.models import  Vinos

class Buscar(forms.Form):
    marca = forms.CharField(max_length=100)

class VinoForm(forms.ModelForm):
  class Meta:
    model = Vinos
    fields = ['marca', 'provincia', 'año']
