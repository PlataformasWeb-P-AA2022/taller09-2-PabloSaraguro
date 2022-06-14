from django.db import models


class Equipo(models.Model):
   
    nombre = models.CharField(max_length=30)
    siglas = models.CharField(max_length=30)
    username = models.CharField(max_length=30)
    campeonatos = models.ManyToManyField('Campeonato', through='CampeonatoEquipos')


    def __str__(self):
        return "%s / %s / %s" % (self.nombre, 
                self.siglas,
                self.username)


class Jugador(models.Model):
    
    nombre = models.CharField(max_length=30)
    posicion = models.CharField(max_length=30)
    numero_camiseta = models.IntegerField()
    sueldo = models.IntegerField()

    equipo = models.ForeignKey('Equipo', related_name='losequipos', 
            on_delete=models.CASCADE)

    def __str__(self):
        return "%s, %s, %d,  %s - %s" % (self.nombre, 
                self.posicion,
                self.numero_camiseta,
                self.sueldo,
                self.equipo.nombre)


class Campeonato(models.Model):
   
    nombre_campeonato = models.CharField(max_length=30)
    auspiciante = models.CharField(max_length=30)

    equipos = models.ManyToManyField('Equipo', through='CampeonatoEquipos')

    def __str__(self):
        return "%s - %s" % \
                (self.nombre_campeonato, self.auspiciante)


class CampeonatoEquipos(models.Model):
 
    anio = models.IntegerField()
    equipo = models.ForeignKey('Equipo', related_name='loscampeonatos', 
            on_delete=models.CASCADE)
    campeonato_equip = models.ForeignKey('Campeonato', related_name='loscampeonatos', 
            on_delete=models.CASCADE)

    def __str__(self):
        return "%d / %s / %s" % \
                (self.anio, self.equipo.nombre, self.campeonato_equip.nombre)
