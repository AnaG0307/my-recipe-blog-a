from . import views
from django.urls import path


urlpatterns = [
    path('', views.Recipe_List_View.as_view(), name='home'),
    path('<slug:slug>/', views.RecipePost.as_view(), name='recipe_post'),
    path('favourite/<int:slug>/', views.favourite_recipe, name='saved_recipes'),
    path('favourite/', views.favourite_list, name='favourite_list'),
]
