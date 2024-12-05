from django.db import models

class Product(models.Model):
    name = models.TextField(max_length=200, verbose_name='nombre')
    description = models.TextField(max_length=300, verbose_name="descripcion")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="precio")
    available = models.BooleanField(default=True, verbose_name="disponibilidad")
    photo = models.ImageField(null =True, blank= True, verbose_name="foto", upload_to='logos/')

    def __str__(self) -> str:
        return f'{self.name}'
    