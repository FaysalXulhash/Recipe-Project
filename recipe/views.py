from django.shortcuts import render, redirect
from .models import Recipe


def register(request):
    return render(request, 'recipe/base.html')

def about(request):
    return render(request, 'recipe/about.html')

def recipe (request):
    if request.method == 'POST':
        data = request.POST

        recipe_name = data.get('recipe_name')
        recipe_description = data.get('recipe_description')
        recipe_image = request.FILES.get('recipe_image')

        Recipe.objects.create(
            recipe_name = recipe_name,
            recipe_description = recipe_description,
            recipe_image = recipe_image,
        )
        return redirect('recipe-home')
    context = {'recipes': Recipe.objects.all()}

        
    return render(request, 'recipe/add_recipe.html', context)

def home(request):
    context = {'recipes': Recipe.objects.all()}
    ordering = ['-recipe_description']
    return render (request, 'recipe/home.html', context)