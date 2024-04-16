from django.db import models

# Create your models here.

class Animal(models.Model):

    mid = models.SmallAutoField(primary_key=True)
    name = models.CharField(max_length=20, null=False, blank=False, verbose_name='animal')
    type = models.CharField(max_length=30, null=False)
    location = models.CharField(max_length=20, null=True, default='earth')

    def __str__(self):
        return f'{self.mid}->{self.name}'


class Owner(models.Model):

    id = models.SmallAutoField(primary_key=True)
    name = models.CharField(max_length=20, null=False, blank=False, verbose_name='owner_name')

    def __str__(self):
        return f'{self.name}'
