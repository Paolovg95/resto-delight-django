from django.db import models

# Create your models here.

class Ingredient(models.Model):
    price = models.DecimalField(decimal_places=2, max_digits=4)
    quantity = models.IntegerField()
    status = models.CharField(max_length=20)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
