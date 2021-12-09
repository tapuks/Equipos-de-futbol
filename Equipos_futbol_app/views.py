from django.shortcuts import render

# Create your views here.
from Equipos_futbol_app.models import Equipo, Plantilla, Trofeos


def home(request):
    equipos=Equipo.objects.all()


    return render(request, 'home.html', {"equipos":equipos})



def plantilla(request, id_equipo):
    plantilla = Plantilla.objects.filter(equipo_id=id_equipo)
    equipo = Equipo.objects.get(id=id_equipo)
    trofeos = Trofeos.objects.filter(equipo_id = id_equipo)
    copa_rey = 0
    copa_liga = 0
    copa_uefa = 0
    copa_europa = 0
    for trofeo in trofeos:
        copa_rey = trofeo.copa_rey
        copa_liga = trofeo.copa_liga
        copa_uefa = trofeo.copa_uefa
        copa_europa = trofeo.copa_europa



    return render(request, 'plantilla.html', {'plantilla': plantilla, 'equipo': equipo, 'trofeos': trofeos, 'range_copa_rey': range(copa_rey),
    'range_copa_liga': range(copa_liga), 'range_copa_uefa': range(copa_uefa), 'range_copa_europa': range(copa_europa)} )

