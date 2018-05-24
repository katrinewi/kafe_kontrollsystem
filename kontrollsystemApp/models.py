from django.db import models

#The cafe class, has methods to handle when a product is bought and when cash is reset
class Cafe(models.Model):
    cash = models.FloatField(default=500)
    def deposit(self, productPrice):
        self.cash += productPrice
        self.save()
    def reset(self):
        self.cash = 0
        self.save()

#The product class, has foreignkey in the cafe class
class Product(models.Model):
    productName = models.CharField(max_length=200)
    productPrice = models.FloatField()
    numbersSold = models.IntegerField(default=0)
    belongsTo = models.ForeignKey(Cafe, on_delete=models.CASCADE, default=Cafe.objects.first().id)

    def __str__(self):
        return self.productName

    def buy(self):
        self.numbersSold += 1
        if self.belongsTo:
            self.belongsTo.deposit(self.productPrice)
        self.save()
