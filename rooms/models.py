from django.db import models

from services.models import Service

# Create your models here.
class House(models.Model):
    name = models.CharField(max_length=50, verbose_name='nombre')
    about = models.TextField(verbose_name='descripción')
    email = models.EmailField(verbose_name='correo', null=True, blank=True)
    address = models.CharField(max_length=150, verbose_name='dirección')
    images = models.ImageField(upload_to='house', verbose_name='imágenes')
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación", null=True, blank=True)
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición", null=True, blank=True)

    class Meta:
        verbose_name = 'casa'
        verbose_name_plural = 'casa'
        
    def __str__(self):
        return self.name
        
class Room(models.Model):
    name = models.CharField(max_length=100, verbose_name='nombre')
    description = models.TextField(verbose_name='descripción')
    images = models.ImageField(upload_to='rooms', verbose_name='imágenes')
    house = models.ForeignKey(House, on_delete=models.CASCADE, verbose_name='casa', null=True, blank=True, related_name='get_house_rooms')
    services = models.ManyToManyField(Service, verbose_name='servicios', related_name='get_service_rooms')
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación", null=True, blank=True)
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición", null=True, blank=True)
    
    class Meta:
        verbose_name = 'habitación'
        verbose_name_plural = 'habitaciones'
        
    def __str__(self):
        return self.name