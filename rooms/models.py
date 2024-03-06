from django.db import models

# Create your models here.
class House(models.Model):
    name = models.CharField(max_length=50, verbose_name='nombre')
    description = models.TextField(verbose_name='descripción')
    address = models.CharField(max_length=150, verbose_name='dirección')
    images = models.ImageField(upload_to='house', verbose_name='imágenes')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'casa'
        
class Room(models.Model):
    name = models.CharField(max_length=100, verbose_name='nombre')
    description = models.TextField(verbose_name='descripción')
    images = models.ImageField(upload_to='rooms', verbose_name='imágenes')
    # services = models.ManyToManyField()
    
    class Meta:
        verbose_name = 'habitación'
        verbose_name_plural = 'habitaciones'