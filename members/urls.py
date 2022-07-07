from django.urls import path
from .views import (
    login_user,
    logout_user,
    register_user,
    create_ingredient,
    view_ingredients,
    view_recipes
)
urlpatterns = [
    path('login_user', login_user, name="login"),
    path('logout_user', logout_user, name='logout'),
    path('register_user', register_user, name="register_user"),
    path('create_ingredient', create_ingredient, name="create_ingredient"),
    path('ingredients', view_ingredients, name="ingredients"),
    path('recipes', view_recipes, name="recipes")
]
