from .models import UserRecipe
from django import forms


class UrecipeForm(forms.ModelForm):
    class Meta:
        model = UserRecipe
        fields = ('title', 'image', 'content', 'ingredients_list')
