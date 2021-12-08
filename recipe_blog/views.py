from django.shortcuts import render
from django.views import generic
from .models import Recipe


class Recipe_List_View(generic.ListView):
    model = Recipe
    template_name = 'index.html'
    queryset = Recipe.objects.filter(approved=1, public_private=1)
    paginate_by = 12
