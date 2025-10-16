from django.http import HttpResponse
from django.template import loader

def recipes(request):
    template = loader.get_template('recipes.html')
    return HttpResponse(template.render())

def searchRecipes(request):
    template = loader.get_template('search.html')
    return HttpResponse(template.render())