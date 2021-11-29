from django.urls import path
from recipe_blog.models import Recipe

urlpatterns = [
    path('', RecipeListView.as_view(), name='home'),
]