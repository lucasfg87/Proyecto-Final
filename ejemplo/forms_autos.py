from django import forms
from ejemplo.models import  Autos

class Buscar(forms.Form):
    marca = forms.CharField(max_length=100)

class AutoForm(forms.ModelForm):
  class Meta:
    model = Autos
    fields = ['marca', 'modelo', 'año']
