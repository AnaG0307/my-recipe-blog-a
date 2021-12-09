from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Recipe, Comment
from .forms import CommentForm


class Recipe_List_View(generic.ListView):
    model = Recipe
    template_name = 'index.html'
    queryset = Recipe.objects.filter(approved=1)
    paginate_by = 12


class RecipePost(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Recipe.objects.filter(approved=1)
        recipe = get_object_or_404(queryset, slug=slug)
        liked = False
        if recipe.likes.filter(id=self.request.user.id).exists():
            liked = True
        context = {
            'recipes': recipe,
            'liked': liked,
            'comment_form': CommentForm()

        }
        return render(request, 'recipe_post.html', context)
    
    def post(self, request, slug, *args, **kwargs):
        queryset = Recipe.objects.filter(approved=1)
        recipe = get_object_or_404(queryset, slug=slug)
        liked = False
        if recipe.likes.filter(id=self.request.user.id).exists():
            liked = True
        context = {
            'recipes': recipe,
            'liked': liked,
            'comment_form': CommentForm()

        }
        return render(request, 'recipe_post.html', context)


class RecipeComment(View):

    def get(self, request, *args, **kwargs):
        user_comment = get_object_or_404(Comment)
        context = {
            'comments': user_comment,
        }

        return render(request, 'recipe_post.html', context)
