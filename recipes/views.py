from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from utils.recipe.factory import make_recipe

def home(request):
    return render(request,'recipes/pages/recipe-view.html',context={'recipe':[ make_recipe() for _ in range(10)]})

def recipe(request, id):
    return render(request, 'recipes/pages/recipe-view.html', context={
        'name': 'Luiz Otávio',
        'recipe': make_recipe(),
    })