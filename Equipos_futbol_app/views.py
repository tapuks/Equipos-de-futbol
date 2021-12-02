from django.shortcuts import render

# Create your views here.
from Equipos_futbol_app.models import Equipo, Plantilla


def home(request):
    equipos=Equipo.objects.all()
    plantillas= Plantilla.objects.all()

    return render(request, 'home.html', {"equipos":equipos, 'plantillas':plantillas})

