from . import views
from django.urls import path


urlpatterns = [
    path('', views.Recipe_List_View.as_view(), name='home'),
    path('<slug:slug>/', views.RecipePost.as_view(), name='recipe_post'),
    path('like/<slug:slug>/', views.PostLike.as_view(), name='post_like'),
    # path('favourite/<int:slug>/', views.favourite_recipe, name='favourite_recipe'),
    # path('myrecipes/', views.favourite_list, name='favourite_list'),
]
