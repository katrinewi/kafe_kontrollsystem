from django.db import models

class Product(models.Model):
    productName = models.CharField(max_length=200)
    productPrice = models.FloatField()
    numbersSold = models.IntegerField(default=0)
    def __str__(self):
        return self.productName
