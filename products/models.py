from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.TextField(max_length=160, verbose_name="nombre")
    description = models.TextField(max_length=500, verbose_name="descripción")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="precio")
    available = models.BooleanField(default=True)
    picture = models.ImageField(upload_to='media/', verbose_name="imagen", null=True, blank=True)
    
    def __str__(self):
        return self.name