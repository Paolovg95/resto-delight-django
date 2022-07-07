from multiprocessing import context
import re
from django.shortcuts import render
from menus.models import CategoryMenu, Recipe
from django.db.models import Q

import pandas as pd

# Create your views here.
def home_view(request):

    return render(request, 'home.html',{})

def about_view(request):

    return render(request, 'about.html', {})

def dashboard_admin(request):
    recipes = Recipe.objects.all()[:4]
    category = CategoryMenu.objects.exclude(Q(name="Appetizers") | Q(name="Drinks")).values() #  Return Query Set
    data = pd.DataFrame(category)
    list = data.name.tolist() # DataFrame Column 'Name' to list
    context = {
        'recipes': recipes,
        'category': list
    }
    return render(request, 'admin_dashboard.html', context)