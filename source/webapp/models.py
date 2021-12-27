from django.db import models

# Create your models here.


class Product(models.Model):
    CATEGORY_CHOISES = [
        ('other', 'Other'),
        ('phones', 'Phones'),
        ('headPhones', 'Head phones'),
        ('memory', 'Memory'),
        ('hdd', 'HDD')
    ]
    title = models.CharField(max_length=100, null=False, blank=False, verbose_name='Название')
    description = models.TextField(max_length=2000, null=False, blank=True, verbose_name='Описание')
    category = models.TextField(max_length=100, null=False, blank=False, choices=CATEGORY_CHOISES, default='other', verbose_name='Категория')
    remainder = models.PositiveIntegerField(null=True, blank=True)
    cost = models.DecimalField(null=False, blank=False, max_digits=7, decimal_places=2)

    def __str__(self) -> str:
        return "{}. {} {}".format(self.pk, self.title, self.cost)