from django.contrib import admin
from .models import Link
# Register your models here.

# Por defecto el administrador no muestra los campos de creación y
# actualización
# cuando son definidos auto_now_add o auto_now, por lo tanto se debe
# crear una clase que herede de las configuraciones y se modifiquen algunas


class LinkAdmin(admin.ModelAdmin):
    # Se sobre escribe el atributo readonly_fields que es una tupla
    readonly_fields = ('created', 'updated')


# Se debe asignar al administrador la nueva configuración
# admin.site.register(Project)
admin.site.register(Link, LinkAdmin)
