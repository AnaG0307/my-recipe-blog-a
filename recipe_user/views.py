from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import UserRecipe
from .forms import UrecipeForm


class UserList(generic.ListView):
    model = UserRecipe
    queryset = UserRecipe.objects.filter(public_private=0)
    template_name = 'recipe_list_user.html'
    paginate_by = 9


def add_recipe(request):
    submitted = False
    form = UrecipeForm
    if request.method == 'POST':
        form = UrecipeForm(request.POST)
        if form.is_valid():
            form.instance.name = request.user.username
            form.save()
            return HttpResponseRedirect('/add_recipe?Submitted=True')
        else:
            form = UrecipeForm()
    return render(request, 'recipe_create_user.html', {'form': form, 'submitted': submitted})
