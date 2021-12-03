from django.contrib import admin

# Register your models here.
from Equipos_futbol_app.models import Equipo, Plantilla, Trofeos

admin.site.register(Equipo)
admin.site.register(Plantilla)
admin.site.register(Trofeos)