from . import views
from django.urls import path, include
from .views import RecipeListView


urlpatterns = [
    path('', RecipeListView.as_view(), name='home'),
    path('', include('recipe_blog.urls'), name='recipe_blog_urls'),
]
