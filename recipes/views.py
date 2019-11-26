from django.shortcuts import render, redirect, HttpResponseRedirect, reverse
from .models import Author, Recipe
from recipebox.templates.forms.form import NewAuthor, NewRecipe, Login
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


# if the user just goes to the website it will redirect to the recipes app
def home(request):
    return render(request, 'home.html')


# Handling the recipe(s) views
@login_required
def recipes(request):
    recipes = Recipe.objects.all()
    context = {'recipes': recipes}
    return render(request, 'recipes/index.html', context)


@login_required
def recipe(request, id):
    recipe = Recipe.objects.get(id=id)
    user = request.user
    print(user)
    print(recipe.author)
    return render(request, 'recipes/recipe_detail.html', {'recipe': recipe, 'user': user})


# handling the author(s) views
@login_required
def authors(request, id):
    author = Author.objects.get(id=id)
    recipes = Recipe.objects.filter(author=id)
    
    context = {
        'author': author,
        'recipes': recipes
        }
    return render(request, 'authors/author_detail.html', context)


# handling new data forms
@login_required
def new_recipe(request):
    if request.method == 'POST':
        form = NewRecipe(request.POST)

        if form.is_valid():
            data = form .cleaned_data

            Recipe.objects.create(
                title=data['title'],
                author=data['author'],
                description=data['description'],
                time_required=data['time_required'],
                instructions=data['instructions']
            )
            return render(request, 'recipes/index.html')

    else:
        form = NewRecipe()
        context = {'form': form}

    return render(request, 'recipes/new_recipe.html', context)


def new_author(request):
    if request.user.is_staff:
        if request.method == 'POST':
            form = NewAuthor(request.POST)

            if form.is_valid():
                data = form .cleaned_data

                user = User.objects.create_user(
                    username=data['name'],
                    password=data['password']
                )

                Author.objects.create(
                    name=data['name'],
                    bio=data['bio'],
                    user=user
                )
                return render(request, 'auth/register_success.html')

        else:
            form = NewAuthor()
            context = {'form': form}

        return render(request, 'auth/register.html', context)
    else:
        return render(request, 'permissions/unauthorized.html')


def login_user(request):
    if request.method == 'POST':
        form = Login(request.POST)

        if form.is_valid():
            data = form.cleaned_data

            user = authenticate(
                request,
                username=data['username'],
                password=data['password']
            )

            if user:
                login(request, user)
                return redirect('/recipes')
            else:
                form = Login()
                message = "You have entered either the wrong password or username. Please try again"
                context = {'message': message, 'type': 'error', 'form': form}
                return render(request, 'auth/login.html', context)
    else:
        form = Login()
        context = {'form': form}

        return render(request, 'auth/login.html', context)


def logout_user(request):
    logout(request)
    return redirect('/')


# handling the edit tickets
def editrecipeview(request, id):
    html = "generic_form.html"

    instance = Recipe.objects.get(id=id)

    if request.method == "POST":
        form = NewRecipe(request.POST, instance=instance)
        form.save()

        return HttpResponseRedirect('/recipes')
    form = NewRecipe(instance=instance)

    return render(request, html, {'form': form})


# handling favoriting
def favorite(request, id):
    current_user = request.user.author
    target_favorite = Recipe.objects.get(id=id)

    current_user.favorites.add(target_favorite)
    return redirect(request.META.get('HTTP_REFERER', '/'))


def unfavorite(request, id):
    current_user = request.user.author
    target_favorite = Recipe.objects.get(id=id)

    current_user.favorites.remove(target_favorite)
    return redirect(request.META.get('HTTP_REFERER', '/'))

