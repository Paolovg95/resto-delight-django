import re
from django.shortcuts import render

# Create your views here.
def home_view(request):

    return render(request, 'home.html',{})

def about_view(request):

    return render(request, 'about.html', {})

def dashboard_admin(request):

    return render(request, 'admin_dashboard.html', {})