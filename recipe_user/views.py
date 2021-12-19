from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic, View
from django.http import HttpResponseRedirect
from django.template.defaultfilters import slugify
from django.contrib import messages
from .models import UserRecipe
from .forms import UrecipeForm


class UserList(generic.ListView):
    model = UserRecipe
    queryset = UserRecipe.objects.filter(public_private=0).order_by("-created_on")
    template_name = 'recipe_list_user.html'
    paginate_by = 9


def add_recipe(request):
    submitted = False
    form = UrecipeForm()
    if request.method == 'POST':
        form = UrecipeForm(request.POST, request.FILES)
        if form.is_valid():
            new_recipe = form.save(commit=False)
            new_recipe.slug = slugify(new_recipe.title)
            new_recipe.save()
            messages.info(request, ('Your recipe is been CREATED successfully!'))
            return HttpResponseRedirect('/myrecipes?Submitted=True')
        else:
            form = UrecipeForm()
            if 'submitted' in request.GET:
                submitted = True
    return render(request, 'recipe_create_user.html', {
        'form': form,
        'submitted': submitted
        })


class UrecipeDetail(View):
    def get(self, request, slug, *args, **kwargs):
        new_post = get_object_or_404(UserRecipe, slug=slug)
        form = UrecipeForm(instance=new_post)
        context = {
            'new_post': new_post,
            'form': form
        }
        return render(request, 'recipe_post_user.html', context)


def edit_recipe(request, slug):
    item = get_object_or_404(UserRecipe, slug=slug)
    if request.method == 'POST':
        form = UrecipeForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            messages.info(request, ('Your recipe is been UPDATED successfully!'))
            return redirect('myrecipes')
    form = UrecipeForm(instance=item)
    context = {
        'item': item,
        'form': form
        }
    return render(request, 'recipe_edit_user.html', context)


def delete_recipe(request, slug):
    item = get_object_or_404(UserRecipe, slug=slug)
    item.delete()
    messages.info(request, ('Your recipe is been DELETED successfully!'))
    return redirect('myrecipes')
