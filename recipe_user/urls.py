from . import views
from django.urls import path


urlpatterns = [
    path('myrecipes/', views.UserList.as_view(), name='myrecipes'),
    path('myrecipes/createform', views.UserList.as_view(), name='createform'),
]
