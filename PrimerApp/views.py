from django.shortcuts import render

from PrimerApp.models import Familiar, Amigos, colegas
from PrimerApp.forms import Buscar, FamiliarForm, colegaForm # <--- NUEVO IMPORT
from django.views import View # <-- NUEVO IMPORT 


def index(request):
    return render(request, "PrimerApp/saludar.html")


def monstrar_familiares(request):
    lista_familiares = Familiar.objects.all()
    return render(request, "PrimerApp/familiares.html", {"lista_familiares": lista_familiares})


class BuscarFamiliar(View):

    form_class = Buscar
    template_name = 'PrimerApp/buscar.html'
    initial = {"nombre":""}

    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data.get("nombre")
            lista_familiares = Familiar.objects.filter(nombre__icontains=nombre).all() 
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form':form, 
                                                        'lista_familiares':lista_familiares})
        return render(request, self.template_name, {"form": form})
    

class AltaFamiliar(View):

    form_class = FamiliarForm
    template_name = 'PrimerApp/alta_familiar.html'
    initial = {"nombre":"", "direccion":"", "numero_pasaporte":""}

    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            msg_exito = f"se cargo con éxito el familiar {form.cleaned_data.get('nombre')}"
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form':form, 
                                                        'msg_exito': msg_exito})
        
        return render(request, self.template_name, {"form": form})


def mostrar_amigos(request):
  lista_amigos = Amigos.objects.all()
  return render(request, "PrimerApp/amigos.html", {"lista_amigos": lista_amigos})


def mostrar_colegas(request):
  lista_colegas = colegas.objects.all()
  return render(request, "PrimerApp/colegas.html", {"lista_colegas": lista_colegas})

class Altacolega(View):

    form_class = colegaForm
    template_name = 'PrimerApp/alta_colega.html'
    initial = {"nombre":"", "direccion":"", "numero_de_telefono":""}

    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            msg_exito = f"se cargo con éxito el colega {form.cleaned_data.get('nombre')}"
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form':form, 
                                                        'msg_exito': msg_exito})
        
        return render(request, self.template_name, {"form": form})