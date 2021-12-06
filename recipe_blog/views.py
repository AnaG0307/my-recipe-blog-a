from django.shortcuts import render
from django.views.generic import ListView
from .models import Recipe


class Recipe_List_View(ListView):
    model = Recipe
    template_name = 'index.html'
    paginate_by = 9
