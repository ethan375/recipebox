from django.shortcuts import render, redirect
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


def authors(request, id):
    author = Author.objects.get(id=id)
    recipes = Recipe.objects.filter(author=id)
    context = {
        'author': author,
        'recipes': recipes
        }
    return render(request, 'authors/author_detail.html', context)


def home(request):
    return redirect('/recipes')
