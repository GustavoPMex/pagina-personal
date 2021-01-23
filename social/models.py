from django.db import models

# Create your models here.

class link(models.Model):
    key = models.SlugField(max_length=100, unique=True, verbose_name='Nombre clave')
    name = models.CharField(max_length=200, verbose_name='Red social')
    url = models.URLField(max_length=200, verbose_name='Enlace', null= True, blank = True)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de modificación')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'enlace'
        verbose_name_plural = 'enlaces'
        ordering = ['-name']