from . import views
from django.urls import path


urlpatterns = [
    path('myrecipes/', views.UserPostList.as_view(), name='myrecipes'),
    ]
