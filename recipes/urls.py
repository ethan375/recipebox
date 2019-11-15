from django.urls import path
from . import views


app_name = 'recipes'
urlpatterns = [
    path('', views.recipes, name='index'),
    path('<int:id>', views.recipe, name='recipe_detail'),
    path('authors/', views.authors, name='index')
]