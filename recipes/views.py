from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect, get_object_or_404
from .models import Recipe

def recipes(request):
    recipes = Recipe.objects.all().values()
    context = {
        'recipes': recipes,
    }
    return render(request, 'recipes.html', context)

def searchRecipes(request):
    return render(request, 'search.html')

def addRecipe(request):
    if request.method == 'POST':
        dishName = request.POST.get('dishName', '').strip()
        creatorName = request.POST.get('creatorName', '').strip()
        ingredients = request.POST.getlist('ingredients')
        # strip whitespace and remove empty strings
        ingredients = [i.strip() for i in ingredients if i and i.strip()]
        try:
            estimatedTime = int(request.POST.get('estimatedTime', 0))
        except ValueError:
            estimatedTime = 0
        directions = request.POST.get('directions', '').strip()

        # add recipe to database
        Recipe.objects.create(
            dishName=dishName,
            creatorName=creatorName,
            ingredients=ingredients,
            estimatedTime=estimatedTime,
            directions=directions,
        )

        return redirect('recipes')
    return render(request, 'addRecipe.html')

def updateRecipe(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    if request.method == 'POST':
        dishName = request.POST.get('dishName', '').strip()
        creatorName = request.POST.get('creatorName', '').strip()
        ingredients = request.POST.getlist('ingredients')
        # strip whitespace and remove empty strings
        ingredients = [i.strip() for i in ingredients if i and i.strip()]
        try:
            estimatedTime = int(request.POST.get('estimatedTime', 0))
        except ValueError:
            estimatedTime = 0
        directions = request.POST.get('directions', '').strip()

        # update recipe and save to database
        recipe.dishName = dishName
        recipe.creatorName = creatorName
        recipe.ingredients = ingredients
        recipe.estimatedTime = estimatedTime
        recipe.directions = directions
        recipe.save()

        return redirect('recipes')
    
    context = {
        'recipe': recipe
    }
    return render(request, 'updateRecipe.html', context)