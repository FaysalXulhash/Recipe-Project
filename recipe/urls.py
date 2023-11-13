from django.urls import path
from .views import about, recipe, home

urlpatterns = [
    path('about/', about, name='recipe-about'),
    path('recipe/', recipe, name='add-recipe'),
    path('', home, name='recipe-home'),

]
