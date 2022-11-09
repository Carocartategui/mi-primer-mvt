from django import forms
from PrimerApp.models import Familiar, colegas

class Buscar(forms.Form):
    nombre = forms.CharField(max_length=100)

class FamiliarForm(forms.ModelForm):
  class Meta:
    model = Familiar
    fields = ['nombre', 'direccion', 'numero_pasaporte']

class colegaForm(forms.ModelForm):
  class Meta:
    model = colegas
    fields = ['nombre', 'apellido', 'numero_de_telefono']