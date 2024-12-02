from django.core.validators import MinValueValidator
from django.db import models


class Product(models.Model):
    name = models.CharField(
        'Название продукты',
        max_length=150
    )
    slug = models.SlugField(
        'Url товара',
        max_length=150,
        unique=True
    )
    price = models.IntegerField(
        'Цена продукта',
        validators=[
            MinValueValidator(1)
        ])
    amount = models.IntegerField(
        'Осталось',
        validators=[
            MinValueValidator(0),
        ]
    )


class Category(models.Model):
    name = models.CharField(
        'Название категории',
        max_length=50
    )
    slug = models.SlugField(
        'Url категории',
        max_length=50,
        unique=True
    )
