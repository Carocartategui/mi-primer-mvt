from django.shortcuts import render

from PrimerApp.models import Familiar


def index(request):
    return render(request, "PrimerApp/saludar.html")


def monstrar_familiares(request):
    lista_familiares = Familiar.objects.all()
    return render(request, "PrimerApp/familiares.html", {"lista_familiares": lista_familiares})