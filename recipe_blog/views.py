from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import Recipe
from .forms import CommentForm


class Recipe_List_View(generic.ListView):
    model = Recipe
    template_name = 'index.html'
    queryset = Recipe.objects.filter(approved=1)
    paginate_by = 9


class RecipePost(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Recipe.objects.filter(approved=1)
        recipe = get_object_or_404(queryset, slug=slug)
        comments = recipe.comments.filter(approved=True).order_by("-created_on")
        liked = False
        if recipe.likes.filter(id=self.request.user.id).exists():
            liked = True
        context = {
            'recipe': recipe,
            'liked': liked,
            'commented': False,
            'comments': comments,
            'comment_form': CommentForm(),
        }
        return render(request, 'recipe_post.html', context)

    def post(self, request, slug, *args, **kwargs):
        queryset = Recipe.objects.filter(approved=1)
        recipe = get_object_or_404(queryset, slug=slug)
        liked = False
        if recipe.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.recipe_title = recipe
            comment.save()
        else:
            comment_form = CommentForm()

        context = {
            'recipe': recipe,
            'liked': liked,
            'commented': True,
            'comment_form': CommentForm()
        }

        return render(request, 'recipe_post.html', context)


class PostLike(View):
    def post(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Recipe, slug=slug)
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse('recipe_post', args=[slug]))

# @login_required
# def favourite_list(request):
#     saved = Recipe.objects.filter(favourite=request.user)
#     return render(request, 'saved_recipes.html', {
#         'saved': saved
#         })


# @login_required
# def favourite_recipe(request, slug):
#     post = get_object_or_404(Recipe, slug=slug)
#     if post.favourite.filter(id=request.user.id).exists():
#         post.favourite.remove(request.user)
#     else:
#         post.favourite.add(request.user)
#     return HttpResponseRedirect(request.META['HTTP_REFERER'])
