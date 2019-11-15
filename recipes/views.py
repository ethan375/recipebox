from django.shortcuts import render
from .models import Author, Recipe


def recipes(request):
    recipes = Recipe.objects.all()
    context = {'recipes': recipes}
    return render(request, 'recipes/index.html', context)


def recipe(request, id):
    recipe = Recipe.objects.get(id=id)
    context = {'recipe': recipe}
    print(recipe)
    return render(request, 'recipes/recipe_detail.html', context)


def authors(request):
    authors = Author.objects.all()
    context = {'authors': authors}
    return render(request, 'authors/index.html', context)

