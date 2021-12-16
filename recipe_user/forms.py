from django import forms
from django.forms import ModelForm
from .models import UserRecipe


# Create a user personal recipe
class UrecipeForm(ModelForm):
    class Meta:
        model = UserRecipe
        fields = ('title', 'image', 'content', 'ingredients_list')
