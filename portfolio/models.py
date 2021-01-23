from django.db import models

# Create your models here.

class project(models.Model):
    title = models.CharField(max_length=50, verbose_name='Titulo')
    image = models.ImageField(verbose_name='Imagen', upload_to='projects')
    description = models.CharField(max_length=150, verbose_name='Descripción')
    url = models.URLField(null=True, blank=True, verbose_name='Link')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de modificación')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'proyecto'
        verbose_name_plural = 'proyectos'
        ordering = ['-created']