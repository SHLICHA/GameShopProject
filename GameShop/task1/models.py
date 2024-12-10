from django.db import models


class Buyer(models.Model):
    name = models.CharField(
        verbose_name='Логин покупателя',
        max_length=255
    )
    balance = models.DecimalField(
        verbose_name='Балансе',
        default=0.00,
        decimal_places=2,
        max_digits=6
    )
    age = models.IntegerField(
        verbose_name='Возраст покупателя'
    )

    class Meta:
        ordering = ["name"]
        verbose_name = "Покупатель"
        verbose_name_plural = "Покупатели"

    def __str__(self):
        return self.name


class Game(models.Model):
    title = models.CharField(
        verbose_name='Название игры',
        max_length=255
    )
    cost = models.DecimalField(
        verbose_name='Стоимость',
        decimal_places=2,
        max_digits=6
    )
    size = models.DecimalField(
        verbose_name='Размер файлов игры',
        decimal_places=2,
        max_digits=6
    )
    description = models.TextField(
        verbose_name='Описание'
    )
    age_limited = models.BooleanField(
        verbose_name='Ограничение 18+',
        default=False
    )
    buyer = models.ManyToManyField(
        Buyer,
        verbose_name='Покупатели',
        related_name='buyers'
    )

    class Meta:
        verbose_name = "Игра"
        verbose_name_plural = "Игры"

    def __str__(self):
        return self.title
