from django.db import models

# Create your models here.


class Page (models.Model):

    title = models.CharField(max_length=200, verbose_name='título')
    content = models.TextField(verbose_name='contenido')
    created = models.DateTimeField(auto_now_add=True,
                                   verbose_name='Fecha creación')
    updated = models.DateTimeField(auto_now=True,
                                   verbose_name='Fecha modificación')

    # Para adicionar metada datos a la clase se debe crear una subclases
    class Meta:
        # Se adicionan atributos especiales para que el administrador
        # tenga esas descripciones
        verbose_name = 'página'
        verbose_name_plural = 'páginas'
        # Por defecto ordena ascendentemente, para hacerlo desce se pone
        # configuraciones antes del nombre del campo
        ordering = ['title']

    # Para adicionar un campo identificador en la pantalla del administrador
    # Se debe sobreescribir el metodo str
    def __str__(self):
        return self.title
