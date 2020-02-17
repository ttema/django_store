from django.db import models


class Product(models.Model):
    ProductID = models.IntegerField()
    Name = models.CharField(max_length=100)
    Description = models.CharField(max_length=300)
    Price = models.DecimalField(max_digits=7, decimal_places=2)
    Category = models.CharField(max_length=100)

    def category(self):
        return self.Category
