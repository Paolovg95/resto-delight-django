from django.contrib import admin
from menus.models import (
    CategoryMenu, 
    MenuItem, 
    Recipe, 
    Ingredient,
    CategoryIngredient)

# Register your models here.
admin.site.register(CategoryMenu)
admin.site.register(CategoryIngredient)
admin.site.register(Ingredient)
admin.site.register(MenuItem)
admin.site.register(Recipe)
