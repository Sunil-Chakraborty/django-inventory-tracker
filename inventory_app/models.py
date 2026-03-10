from django.db import models

class InventoryItem(models.Model):
    item = models.CharField(max_length=200)
    category = models.CharField(max_length=100)
    quantity = models.IntegerField()
    price = models.FloatField()
    date = models.DateField()
 

class SheetData(models.Model):
    name = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    date = models.DateField()

    def __str__(self):
        return self.name    