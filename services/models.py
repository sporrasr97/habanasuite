from django.db import models

# Create your models here.
class Service(models.Model):
    title = models.CharField(max_length=200, verbose_name='título')
    content = models.TextField(verbose_name='contenido')
    image = models.ImageField(upload_to='services', verbose_name='imagen')
    created = models.DateTimeField(auto_now_add=True, verbose_name='fecha de creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='fecha de edición')
    
    class Meta:
        verbose_name = 'servicio'
        verbose_name_plural = 'servicios'
        ordering = ['created']
        
    def __str__(self):
        return self.title