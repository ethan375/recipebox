from django import forms
# from recipes.models import Author


class NewAuthor(forms.Form):
    name = forms.CharField(max_length=30)
    bio = forms.CharField(widget=forms.Textarea)
    password = forms.CharField(widget=forms.PasswordInput)


class NewRecipe(forms.Form):
    title = forms.CharField(max_length=30)
    # authors = [(a.id, a.name) for a in Author.objects.all()]
    # author = forms.ChoiceField(choices=authors)
    description = forms.CharField(widget=forms.Textarea)
    time_required = forms.CharField(widget=forms.Textarea)
    instructions = forms.CharField(widget=forms.Textarea)


class Login(forms.Form):
    username = forms.CharField(max_length=30)
    password = forms.CharField(widget=forms.PasswordInput)
