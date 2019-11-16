from django.shortcuts import render, redirect
from .models import Author, Recipe
from recipebox.templates.forms.form import NewAuthor, NewRecipe


# if the user just goes to the website it will redirect to the recipes app
def home(request):
    return redirect('/recipes')


# Handling the recipe(s) views
def recipes(request):
    recipes = Recipe.objects.all()
    context = {'recipes': recipes}
    return render(request, 'recipes/index.html', context)


def recipe(request, id):
    recipe = Recipe.objects.get(id=id)
    context = {'recipe': recipe}
    print(recipe)
    return render(request, 'recipes/recipe_detail.html', context)


# handling the author(s) views
def authors(request, id):
    author = Author.objects.get(id=id)
    recipes = Recipe.objects.filter(author=id)
    context = {
        'author': author,
        'recipes': recipes
        }
    return render(request, 'authors/author_detail.html', context)


# handling new data forms
def new_recipe(request):
    if request.method == 'POST':
        form = NewRecipe(request.POST)

        if form.is_valid():
            data = form .cleaned_data

            Recipe.objects.create(
                title = data['title'],
                author = Author.objects.filter(id=data['author']).first(),
                description = data['description'],
                time_required = data['time_required'],
                instructions = data['instructions']
            )
            return render(request, 'thanks.html')

    else:
        form = NewRecipe()
        context = {'form': form}

    return render(request, 'recipes/new_recipe.html', context)


def new_author(request):
    if request.method == 'POST':
        form = NewAuthor(request.POST)

        if form.is_valid():
            data = form .cleaned_data

            Author.objects.create(
                name = data['name'],
                bio = data['bio']
            )
            return render(request, 'thanks.html')

    else:
        form = NewAuthor()
        context = {'form': form}

    return render(request, 'authors/new_author.html', context)