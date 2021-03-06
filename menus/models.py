from pickle import LIST
from unicodedata import category
from django.db import models

class CategoryMenu(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class CategoryIngredient(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class Ingredient(models.Model):
    name = models.CharField(max_length=30)
    category = models.ForeignKey(CategoryIngredient, on_delete=models.CASCADE,null=True)
    price = models.DecimalField(decimal_places=2, max_digits=5)
    unit =  models.CharField(max_length=30)
    quantity = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name


class Recipe(models.Model):
    DONE = 'Done'
    PROCESS = 'In Process'
    LISTED_ON_MENU = 'Listed on Menu'
    STATUS = [
        (DONE, 'Done'),
        (PROCESS, 'In Process'),
        (LISTED_ON_MENU, 'Listed on Menu')
    ]
    title = models.CharField(max_length=30)
    status = models.CharField(max_length=20,null=True,choices=STATUS)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title


class MenuItem(models.Model):
    title = models.CharField(max_length=30)
    category = models.ForeignKey(CategoryMenu, on_delete=models.CASCADE,null=True)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    price = models.DecimalField(decimal_places=2, max_digits=5)
    # status = models.CharField(max_length=10,null=True)

    def __str__(self):
        return self.title
