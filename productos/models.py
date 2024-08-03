from django.db import models

# Create your models here.
class Productos(models.Model):
    Productos = models.CharField(max_length=200)
    Precios = models.FloatField(blank=True)
    Stock = models.IntegerField(blank=True)

    def __str__(self) -> str:
        return self.Productos