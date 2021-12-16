from . import views
from django.urls import path


urlpatterns = [
    path('', views.UserList.as_view(), name='myrecipes'),
    path('<str:title>/', views.UserPost.as_view(), name='user_post'),
    # path('createform/', views.UserList.as_view(), name='createform'),
]
