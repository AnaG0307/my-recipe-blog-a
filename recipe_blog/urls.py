from . import views
from django.urls import path


urlpatterns = [
    path('', views.Recipe_List_View.as_view(), name='home'),
    path('like/<slug:slug>/', views.PostLike.as_view(), name='post_like'),
    path('blog/<slug:slug>/', views.RecipePost.as_view(), name='recipe_post'),
    path('search/', views.search_recipe, name='search_recipe'),
]
