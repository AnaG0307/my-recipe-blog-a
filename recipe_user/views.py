from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic, View
from django.http import HttpResponseRedirect
from django.template.defaultfilters import slugify
from .models import UserRecipe
from .forms import UrecipeForm


class UserList(generic.ListView):
    model = UserRecipe
    queryset = UserRecipe.objects.filter(public_private=0)
    template_name = 'recipe_list_user.html'
    paginate_by = 9


def urecipe_detail(request):
    model = UserRecipe
    return render(request, 'recipe_post_user.html')


def add_recipe(request):
    submitted = False
    form = UrecipeForm
    if request.method == 'POST':
        form = UrecipeForm(request.POST)
        if form.is_valid():
            new_recipe = form.save(commit=False)
            print(new_recipe.content)
            new_recipe.slug = slugify(new_recipe.title)
            print(new_recipe.slug)
            new_recipe.save()
            return HttpResponseRedirect('/myrecipes?Submitted=True')
        else:
            form = UrecipeForm()
            if 'submitted' in request.GET:
                submitted = True


    return render(request, 'recipe_create_user.html', {'form': form, 'submitted': submitted})
