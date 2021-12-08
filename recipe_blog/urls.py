from . import views
from django.urls import path


urlpatterns = [
    path('', views.Recipe_List_View.as_view(), name='home'),
    path('<slug:slug>/', views.RecipePost.as_view(), name='recipe_post'),
]
