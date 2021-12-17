from django.urls import path
from . import views


urlpatterns = [
    path('', views.UserList.as_view(), name='myrecipes'),
    path('add-recipe/', views.add_recipe, name='add-recipe'),
    path('user/<slug:slug>/', views.UrecipeDetail.as_view(),
         name='urecipe-detail'),
]
