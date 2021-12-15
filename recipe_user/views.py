from django.shortcuts import render
from django.views import generic
from .models import UserRecipe
from .forms import UrecipeForm


class UserList(generic.ListView):
    model = UserRecipe
    queryset = UserRecipe.objects.filter(PUBPRI=0)
    template_name = 'recipe_list_user.html'
    paginate_by = 9
