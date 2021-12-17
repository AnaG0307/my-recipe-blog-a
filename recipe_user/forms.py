from django import forms
from .models import UserRecipe


# Create a user personal recipe
class UrecipeForm(forms.ModelForm):
    class Meta:
        model = UserRecipe
        fields = ('title', 'image', 'content', 'ingredients_list')
