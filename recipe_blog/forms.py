from .models import Comment
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)


# class UserRecipeForm(forms.ModelForm):
#     class Meta:
#         model = UserRecipe
#         fields = ['title', 'image', 'content', 'ingredients_list']
