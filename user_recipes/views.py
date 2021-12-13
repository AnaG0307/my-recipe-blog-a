from django.shortcuts import render, redirect
from django.views import generic
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
        title = request.POST.get('item_title')
        ingredients = request.POST.get('item_ingredients')
        content = request.POST.get('item_content')
        UserCreation.objects.create(
            title=title,
            ingredients=ingredients,
            content=content
            )
        return redirect('myrecipes')

    userform = RecipeForm()
    context = {
        'userform': userform
    }
    return render(request, 'recipe_create_user.html', context)
