from multiprocessing import context
import re
from django.shortcuts import render
from menus.models import Category
import pandas as pd

# Create your views here.
def home_view(request):

    return render(request, 'home.html',{})

def about_view(request):

    return render(request, 'about.html', {})

def dashboard_admin(request):
    category = Category.objects.all().values() #  Return Query Set
    data = pd.DataFrame(category)
    list = data.name.tolist() # DataFrame Column 'Name' to list
    context = {
        'object': list
    }
    return render(request, 'admin_dashboard.html', context)