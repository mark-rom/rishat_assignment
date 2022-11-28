from django.db import models


class Item(models.Model):
    class Currency(models.TextChoices):
        USD = 'usd'
        AMD = 'amd'

    name = models.CharField(
        max_length=150, verbose_name='Название'
    )
    description = models.TextField(
        verbose_name='Описание', blank=True
    )
    price = models.IntegerField(
        verbose_name='Цена'
    )
    currency = models.CharField(
        max_length=3, choices=Currency.choices, default=Currency.USD
    )

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.name
