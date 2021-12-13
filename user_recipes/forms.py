from django import forms
from .models import UserCreation


class RecipeForm(forms.ModelForm):
    class Meta:
        model = UserCreation
        fields = ['title', 'image', 'content', 'ingredients_list']
