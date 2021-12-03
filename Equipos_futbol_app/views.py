from django.shortcuts import render

# Create your views here.
from Equipos_futbol_app.models import Equipo, Plantilla


def home(request):
    equipos=Equipo.objects.all()


    return render(request, 'home.html', {"equipos":equipos})



def plantilla(request, id_equipo):
    plantilla = Plantilla.objects.filter(equipo_id=id_equipo)
    equipo = Equipo.objects.get(id=id_equipo)
    return render(request, 'plantilla.html', {'plantilla': plantilla, 'equipo': equipo})

