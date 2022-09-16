from cgi import print_exception
from tkinter import Widget
from unicodedata import category, name
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from menus.models import Ingredient, Recipe

class IngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = ('name', 'category', 'price', 'unit', 'quantity')
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'category': forms.Select(attrs={'class':'form-control'}),
            'price': forms.TextInput(attrs={'class':'form-control'}),
            'unit': forms.TextInput(attrs={'class':'form-control'}),
            'quantity': forms.TextInput(attrs={'class':'form-control'})
        }

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
<<<<<<< HEAD
        fields = ('username', 'first_name', 'last_name','email','password1','password2')

    def __init__(self, *args, **kwargs):
        super(UserRegistrationForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'
=======
        fields = ('username', 'first_name', 'last_name')

class RecipeForm(forms.ModelForm):
    class Meta: 
        model = Recipe
        fields = ('title', 'status')    
        widgets = {
            'title': forms.TextInput(attrs = { 'class': 'form-control'}),
        }
>>>>>>> f046c9d7f2045221cbeb6bd575f81b41bc88af97
