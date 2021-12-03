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
    position_jugador = models.CharField(max_length=55)
    dorsal= models.IntegerField()
    pais = models.CharField(max_length=55, blank=True)
    equipo= models.ForeignKey(Equipo, on_delete=models.CASCADE)

    class Meta:
        verbose_name ='plantilla'
        verbose_name_plural = 'plantillas'

    def __str__(self):
        return str(self.nombre_jugador) + " con dorsal " + str(self.dorsal) + " juega en la posicion de " + str(self.position_jugador)

class Trofeos (models.Model):
    copa_rey = models.IntegerField( blank=True,
        null=True)
    copa_liga = models.IntegerField( blank=True,
        null=True)
    copa_europa= models.IntegerField( blank=True,
        null=True)
    copa_uefa = models.IntegerField( blank=True,
        null=True)
    equipo= models.ForeignKey(Equipo, on_delete=models.CASCADE)

    class Meta:
        verbose_name ='trofeo'
        verbose_name_plural = 'trofeos'

    def __str__(self):
        return str(self.equipo)

    # CLASEEEE TROFEOO HECHA, HACER LA VIEW, URL Y MOSTRAR LOS TROFEOS