from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator, RegexValidator

# Create your models here.
class Producto(models.Model):
    Tipo = models.CharField(
        max_length=20,
        validators=[
            RegexValidator(
                regex='^[A-Za-z]+$',
                message='El tipo solo debe contener letras (sin espacios ni números).'
            )
        ]
    )
    Nombre = models.CharField(
        max_length=20,
        validators=[
            RegexValidator(
                regex='^[A-Za-z0-9 ]+$',
                message='El nombre solo puede contener letras, números y espacios.'
            )
        ]
    )
    Descripcion = models.CharField(
        max_length=100,
        validators=[
            RegexValidator(
                regex='^[A-Za-z0-9,. ]+$',
                message='La descripción solo puede contener letras, números, comas, puntos y espacios.'
            )
        ]
    )
    Stock = models.IntegerField(
        validators=[
            MinValueValidator(0, message='El stock no puede ser negativo.'),
            MaxValueValidator(1000, message='El stock no puede superar las 1000 unidades.')
        ]
    )
    Precio = models.IntegerField(
        validators=[
            MinValueValidator(1, message='El precio debe ser mayor que 0.')
        ]
    )