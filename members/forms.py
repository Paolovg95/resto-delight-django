from cgi import print_exception
from unicodedata import category, name
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from menus.models import Ingredient

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
    email = forms.EmailField()
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name')
