from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic, View
from .models import UserCreation
from .forms import RecipeForm


class UserPostList(generic.ListView):
    model = UserCreation
    template_name = 'recipe_list_user.html'
    paginate_by = 9


def user_recipe(request):
    items = UserCreation.objects.all()
    context = {
        'items': items
    }
    return render(request, 'recipe_list_user.html', context)


def user_create(request):
    if request.method == 'POST':
        userform = RecipeForm(request.POST)
        if userform.is_valid():
            userform.save()
            return redirect('myrecipes')
    userform = RecipeForm()
    context = {
        'userform': userform
    }
    return render(request, 'recipe_create_user.html', context)


class UserPost(View):
    def get(self, request, slug, *args, **kwargs):
        queryset = UserCreation.objects.all()
        user_post = get_object_or_404(queryset, slug=slug)
        context = {
            'userrecipe': userrecipe,
        }
        return render(request, 'recipe_post-user.html', context)
