from django.urls import path
from .views import register, about, recipe, home

urlpatterns = [
    path('', register, name='user-registration'),
    path('about/', about, name='recipe-about'),
    path('recipe/', recipe, name='add-recipe'),
    path('home', home, name='recipe-home'),

]
