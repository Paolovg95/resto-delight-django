from unicodedata import category
from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Recipe(models.Model):
    title = models.CharField(max_length=30)
    status = models.CharField(max_length=10,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title


class MenuItem(models.Model):
    title = models.CharField(max_length=30)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,null=True)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    price = models.DecimalField(decimal_places=2, max_digits=5)
    # status = models.CharField(max_length=10,null=True)

    def __str__(self):
        return self.title
