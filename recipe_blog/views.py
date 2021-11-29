from django.views.generic import ListView
from recipe_blog.models import Recipe


class RecipeListView(ListView):
    model = Recipe
    # queryset = Recipe.objects.filter(status_approved=1).order_by('-created-on')
    template_name = 'templates/base.html'
    # paginated_by = 9
