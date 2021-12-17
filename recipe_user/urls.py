from django.urls import path
from . import views


urlpatterns = [
    path('add-recipe/', views.add_recipe, name='add-recipe'),
    path('', views.UserList.as_view(), name='myrecipes'),
    path('<slug>/', views.UrecipeDetail.as_view(), 
        name='urecipe-detail'),
]
