from django.contrib import admin
from .models import Category, Post

# Register your models here.


class CategoryAdmin (admin.ModelAdmin):
    # Se sobre escribe el atributo readonly_fields que es una tupla
    readonly_fields = ('created', 'updated')

# Link de la documentación con las opciones de ModelAdmin
# https://docs.djangoproject.com/en/2.0/ref/contrib/admin/#modeladmin-options


class PostAdmin (admin.ModelAdmin):
    # Se sobre escribe el atributo readonly_fields que es una tupla
    readonly_fields = ('created', 'updated')
    list_display = ('title', 'author', 'published', 'post_categories')
    # Si se quiere dejar un solo campo se debe dejar una coma de la tupla
    ordering = ('published', 'author')
    # para hacer referencia a un campo ForeignKey en la busqueda
    # es necesario especificar el campo de la otra entidad separado por __
    search_fields = ('title', 'content', 'author__username', 'categories__name')
    list_filter = ('author__username', 'categories__name')

    # Los campos de many to many no se pueden mostrar directamente
    # para esto se crea una función que recorra las categorias asociadas al post
    # y lo une con una coma (,)
    # Para adicionar código html a estos datos se puede consultar este link.
    # https://stackoverflow.com/questions/47953705/how-do-i-use-allow-tags-in-django-2-0-admin
    def post_categories(self, obj):
        return ", ".join([c.name for c in obj.categories.all().order_by('name')])
    post_categories.short_description = 'Categorias'


# Se debe asignar al administrador la nueva configuración
# admin.site.register(Project)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
