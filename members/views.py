<<<<<<< HEAD
from pickletools import read_uint1
from django.shortcuts import render, redirect
=======
from multiprocessing import context
from django.shortcuts import render, redirect, get_object_or_404
>>>>>>> f046c9d7f2045221cbeb6bd575f81b41bc88af97
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .forms import UserRegistrationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Group
from .forms import IngredientForm, RecipeForm
from menus.models import Ingredient, Recipe
# Create your views here.


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            if user.is_superuser or user.is_staff:
                login(request, user)
                return redirect('dashboard')
            else:
                login(request,user)
                return redirect('home')
        else:
            messages.success(request, "There was an error, try again")
            return redirect('login')
    else:
        return render(request, 'authenticate/login.html', {})


<<<<<<< HEAD
=======
def create_ingredient(request):
    form = IngredientForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            ingredient = form.save(commit=False)
            ingredient.save()
            return redirect('ingredients')
    else:
        form = IngredientForm()
    
    context = {
        'form': form 
    }

    return render(request, 'authenticate/create_ingredient.html', context)

def delete_ingredient(request, id=id):
    ingredient = get_object_or_404(Ingredient, id=id)

    if request.method == 'POST':
        ingredient.delete()

        return redirect()
def view_ingredients(request):
    ingredients = Ingredient.objects.all()

    context = { 
        'objects': ingredients
    }
    return render(request, 'authenticate/ingredients.html', context)

def view_recipes(request):
    recipes = Recipe.objects.all()

    context = {
        'recipes': recipes
    }

    return render(request, 'authenticate/recipes.html', context)

def create_recipe(request):
    form = RecipeForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.save()
            return redirect('dashboard')
    else:
        form = RecipeForm()

    context = {
        'form': form
    }
    return render(request, 'authenticate/create_recipe.html', context)

def delete_recipe(request, id=id):
    recipe = get_object_or_404(Recipe, id=id)
    if request.method == 'POST':
        recipe.delete()
        return redirect('recipes')
    
    context = {
        'object': recipe
    }
    return render(request, "authenticate/delete_recipe.html", context)

>>>>>>> f046c9d7f2045221cbeb6bd575f81b41bc88af97
def logout_user(request):
    logout(request)
    messages.success(request,'You were Logged out!')
    return redirect('home')


def register_user(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            login(request, user)
            messages.success(request, 'Registration Successful')
            return redirect('home')

    else:
<<<<<<< HEAD
        form = UserRegistrationForm()

=======
        form = UserCreationForm()
>>>>>>> f046c9d7f2045221cbeb6bd575f81b41bc88af97
    return render(request, 'authenticate/register_user.html', {'form': form})
