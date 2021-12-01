from django.views.generic import ListView
from .models import Recipe


class RecipeListView(ListView):
    model = Recipe
    # queryset = Recipe.objects.filter(status_approved=1).order_by('-created-on')
    template_name = 'index.html'
    # paginated_by = 9
