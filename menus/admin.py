from django.contrib import admin
from menus.models import Category, MenuItem, Recipe

# Register your models here.
admin.site.register(Category)
admin.site.register(MenuItem)
admin.site.register(Recipe)
