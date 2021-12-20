from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import Recipe
from .forms import CommentForm


# Code to render contents created by the site admin
class Recipe_List_View(generic.ListView):
    model = Recipe
    template_name = 'index.html'
    queryset = Recipe.objects.filter(approved=1)
    paginate_by = 9


# Code to get and post the contents created by the site admin and
# post the site users comments and likes on a recipe.
class RecipePost(View):
    def get(self, request, slug, *args, **kwargs):
        queryset = Recipe.objects.filter(approved=1)
        recipe = get_object_or_404(queryset, slug=slug)
        comments = recipe.comments.filter(
                    approved=True).order_by("-created_on")
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


# Code to allow the site user to like/unlike a particular post
class PostLike(View):
    def post(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Recipe, slug=slug)
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse('recipe_post', args=[slug]))


# Code to allow user to aearch for recipes
def search_recipe(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        searched_recipe = Recipe.objects.filter(content__contains=searched)
        return render(request, 'search_recipe.html', {
            'searched': searched,
            'searched_recipe': searched_recipe
            })
    else:

        return render(request, 'search_recipe.html')
