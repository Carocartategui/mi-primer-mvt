from django.shortcuts import render

from PrimerApp.models import Familiar
from PrimerApp.forms import Buscar # <--- NUEVO IMPORT
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