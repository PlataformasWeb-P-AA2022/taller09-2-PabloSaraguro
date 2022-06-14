from django.contrib import admin

# Register your models here.

from futbolec.models import Equipo, Jugador, Campeonato, CampeonatoEquipos


admin.site.register(Equipo)

class JugadorAdmin(admin.ModelAdmin):

    list_display = ('nombre', 'posicion', 'numero_camiseta', 'sueldo', 'equipo')
    search_fields = ('nombre',)
    

admin.site.register(Jugador, JugadorAdmin)

admin.site.register(Campeonato)


class CampeonatoEquiposAdmin(admin.ModelAdmin):


    list_display = ('anio', 'equipo', 'campeonato_equip')
    search_fields = ('equipo__nombre', 'campeonato_equip__nombre')

admin.site.register(CampeonatoEquipos, CampeonatoEquiposAdmin)
