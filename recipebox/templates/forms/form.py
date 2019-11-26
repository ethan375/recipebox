from django import forms
from recipes.models import Author, Recipe


class NewAuthor(forms.Form):
    name = forms.CharField(max_length=30)
    bio = forms.CharField(widget=forms.Textarea)


class NewRecipe(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = [
            'title',
            'author',
            'description',
            'time_required',
            'instructions'
        ]

