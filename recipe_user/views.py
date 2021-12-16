from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import UserRecipe
from .forms import UrecipeForm


class UserList(generic.ListView):
    model = UserRecipe
    queryset = UserRecipe.objects.filter(public_private=0)
    template_name = 'recipe_list_user.html'
    paginate_by = 9


class UserPost(View):
    def get(self, request, title, *args, **kwargs):
        queryset = UserRecipe.objects.filter(public_private=0)
        post = get_object_or_404(queryset, title=title)
        context = {
            'post': post,
        }

        return render(request, 'recipe_post_user.html', context)
