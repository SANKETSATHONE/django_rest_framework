from django.db import models

# Create your models here.


class Products(models.Model):

    name = models.CharField(max_length=20, verbose_name="Product's name",null=False, blank=False)
    brand = models.CharField(verbose_name='Company',max_length=20, null=False, blank=True)
    price = models.FloatField(verbose_name= "Product's cost", null=False)
    quantity = models.IntegerField(null=False, default=1, verbose_name="Product's qty")
    purchase_date = models.DateTimeField(auto_now=True)
    delivery = models.CharField(max_length=20, blank=False)

    def __str__(self):
        return f'{self.name} -> {self.price}'

    def __repr__(self):
        return str(self)
