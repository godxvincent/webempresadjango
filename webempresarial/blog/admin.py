from django.contrib import admin
from .models import Category, Post

# Register your models here.


class CategoryAdmin (admin.ModelAdmin):
    # Se sobre escribe el atributo readonly_fields que es una tupla
    readonly_fields = ('created', 'updated')


class PostAdmin (admin.ModelAdmin):
    # Se sobre escribe el atributo readonly_fields que es una tupla
    readonly_fields = ('created', 'updated')


# Se debe asignar al administrador la nueva configuración
# admin.site.register(Project)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
