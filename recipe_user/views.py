from django.shortcuts import render, get_object_or_404
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


def add_recipe(request):
    submitted = False
    form = UrecipeForm
    if request.method == 'POST':
        form = UrecipeForm(request.POST)
        if form.is_valid():
            new_recipe = form.save(commit=False)
            # print(new_recipe.content)
            new_recipe.slug = slugify(new_recipe.title)
            # print(new_recipe.slug)
            new_recipe.save()
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
