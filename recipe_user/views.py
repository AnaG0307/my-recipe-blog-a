from django.shortcuts import render
from django.views import generic, View
from .models import UserRecipe
from .forms import UrecipeForm


class UserList(generic.ListView):
    model = UserRecipe
    queryset = UserRecipe.objects.filter(public_private=0)
    template_name = 'recipe_list_user.html'
    paginate_by = 9


