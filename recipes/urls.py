from django.urls import path
from . import views


app_name = 'recipes'
urlpatterns = [
    path('', views.home),
    path('recipes', views.recipes, name='index'),
    path('recipe/<int:id>', views.recipe, name='recipe_detail'),
    path('author/<int:id>', views.authors, name='author_detail'),
    path('recipe/new', views.new_recipe, name='new_recipe'),
    path('author/new', views.new_author, name="new_author")
]