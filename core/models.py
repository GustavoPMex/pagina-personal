from django.db import models
from solo.models import SingletonModel

# Create your models here.

# class description(models.Model):
#     description_one = models.CharField(max_length=170, verbose_name='Descripción uno')
#     description_two = models.CharField(max_length=280, verbose_name='Descripción dos')
#     imagen_profile = models.ImageField(verbose_name='Imagen de perfil', upload_to="core")
#     create = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
#     upgrade = models.DateTimeField(auto_now = True, verbose_name='Fecha de modificación')

class description(SingletonModel):
    description_one = models.CharField(max_length=170, verbose_name='Descripción uno')
    description_two = models.CharField(max_length=280, verbose_name='Descripción dos')
    imagen_profile = models.ImageField(verbose_name='Imagen de perfil', upload_to="core")
    create = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    upgrade = models.DateTimeField(auto_now = True, verbose_name='Fecha de modificación')

    def __str__(self):
        return 'Descripción profesional'

    class Meta:
        verbose_name = 'descripcion'
        verbose_name_plural = 'descripciones'
        ordering = ['-create']