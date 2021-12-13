from . import views
from django.urls import path


urlpatterns = [
    path('myrecipes/', views.UserPostList.as_view(), name='myrecipes'),
    path('<slug:slug>/', views.UserPost.as_view(), name='user-post'),
    path('create-recipe/', views.user_create, name='create-recipe'),
    ]
