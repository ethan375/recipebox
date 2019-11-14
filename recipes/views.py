from django.shortcuts import render
from .models import Author, Recipe


def index(request):
    return render(request, 'recipes/index.html')