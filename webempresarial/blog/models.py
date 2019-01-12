from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User
# Create your models here.


class Category (models.Model):

    name = models.CharField(max_length=100, verbose_name='nombre')
    created = models.DateTimeField(auto_now_add=True,
                                   verbose_name='Fecha creación')
    updated = models.DateTimeField(auto_now=True,
                                   verbose_name='Fecha modificación')

    # Para adicionar metada datos a la clase se debe crear una subclases
    class Meta:
        # Se adicionan atributos especiales para que el administrador
        # tenga esas descripciones
        verbose_name = 'categoria'
        verbose_name_plural = 'categoria'
        # Por defecto ordena ascendentemente, para hacerlo desce se pone
        # configuraciones antes del nombre del campo
        ordering = ['-created']

    # Para adicionar un campo identificador en la pantalla del administrador
    # Se debe sobreescribir el metodo str
    def __str__(self):
        return self.name


class Post (models.Model):

    title = models.CharField(max_length=200, verbose_name='titulo')
    content = models.TextField(verbose_name='contenido')
    published = models.DateTimeField(default=now,
                                     verbose_name='Fecha de publicación')
    image = models.ImageField(verbose_name='Imagen', upload_to='blog',
                              null=True, blank=True)
    # el parametro on_delete es obligatorio de django2 en adelante
    # Link documentación django2 sobre ForeignKey
    # https://docs.djangoproject.com/en/2.0/ref/models/fields/#django.db.models.ForeignKey
    # https://docs.djangoproject.com/en/2.0/ref/models/fields/#django.db.models.ForeignKey.on_delete
    author = models.ForeignKey(User, verbose_name='Autor',
                               on_delete=models.CASCADE)
    # Link con docuentación sobre como usar las relaciones many to many
    # https://docs.djangoproject.com/en/2.0/ref/models/fields/#django.db.models.ManyToManyField
    categories = models.ManyToManyField(Category, verbose_name='Categoria')
    created = models.DateTimeField(auto_now_add=True,
                                   verbose_name='Fecha creación')
    updated = models.DateTimeField(auto_now=True,
                                   verbose_name='Fecha modificación')

    # Para adicionar metada datos a la clase se debe crear una subclases
    class Meta:
        # Se adicionan atributos especiales para que el administrador
        # tenga esas descripciones
        verbose_name = 'entrada'
        verbose_name_plural = 'entradas'
        # Por defecto ordena ascendentemente, para hacerlo desce se pone
        # configuraciones antes del nombre del campo
        ordering = ['-created']

    # Para adicionar un campo identificador en la pantalla del administrador
    # Se debe sobreescribir el metodo str
    def __str__(self):
        return self.title
