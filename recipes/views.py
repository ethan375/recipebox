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
@login_required(login_url='/login', redirect_field_name='')
def recipes(request):
    recipes = Recipe.objects.all()
    context = {'recipes': recipes}
    return render(request, 'recipes/index.html', context)


@login_required(login_url='/login', redirect_field_name='')
def recipe(request, id):
    recipe = Recipe.objects.get(id=id)
    context = {'recipe': recipe}
    print(recipe)
    return render(request, 'recipes/recipe_detail.html', context)


# handling the author(s) views
@login_required(login_url='/login', redirect_field_name='')
def authors(request, id):
    author = Author.objects.get(id=id)
    recipes = Recipe.objects.filter(author=id)
    context = {
        'author': author,
        'recipes': recipes
        }
    return render(request, 'authors/author_detail.html', context)


# handling new data forms
@login_required(login_url='/login', redirect_field_name='')
def new_recipe(request):
    if request.method == 'POST':
        form = NewRecipe(request.POST)

        if form.is_valid():
            data = form .cleaned_data

            Recipe.objects.create(
                title = data['title'],
                author = request.user.author,
                description = data['description'],
                time_required = data['time_required'],
                instructions = data['instructions']
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

                user = User.objects.create(
                    username=data['name'],
                    password=data['password']
                )

                Author.objects.create(
                    name = data['name'],
                    bio = data['bio'],
                    user = user
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

            if user is not None:
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
