from django.shortcuts import render, HttpResponse
from django.views import generic
from .models import UserCreation


class UserPostList(generic.ListView):
    model = UserCreation
    template_name = 'recipe_list_user.html'
    paginate_by = 9


def User_Recipe(request):
    items = UserCreation.objects.all()
    context = {
        'items': items
    }
    return render(request, 'recipe_list_user.html', context)
