from django.db import models

# Create your models here.


class Vendor(models.Model):

    name = models.CharField(max_length=20, verbose_name="Vendor's name",null=False, blank=False)
    city = models.CharField(verbose_name='Company',max_length=20, null=False, blank=True)
    charges = models.FloatField(verbose_name= "Vendor's cost", null=False)


    def __str__(self):
        return f'{self.name} -> {self.city}'

    def __repr__(self):
        return str(self)