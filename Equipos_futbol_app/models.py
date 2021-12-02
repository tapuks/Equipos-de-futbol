from turtle import position

from django.db import models

# Create your models here.
class Equipo(models.Model):
    nombre = models.CharField(max_length=55)
    imagen_escudo = models.ImageField(upload_to='equipo', null=True, blank=True)


    class Meta:
        verbose_name ='equipo'
        verbose_name_plural = 'equipos'

    def __str__(self):
        return self.nombre

class Plantilla (models.Model):
    nombre_jugador = models.CharField(max_length=55)
    imagen_jugador = models.ImageField(upload_to='plantilla', null=True, blank=True)
    position_jugador = models.CharField(max_length=55)
    dorsal= models.IntegerField()
    equipo= models.ForeignKey(Equipo, on_delete=models.CASCADE)

    class Meta:
        verbose_name ='plantilla'
        verbose_name_plural = 'plantillas'

    def __str__(self):
        return self.nombre_jugador + " con dorsal " + str(self.dorsal) + " juega en la posicion de " + self.position_jugador
