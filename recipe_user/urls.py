from . import views
from django.urls import path


urlpatterns = [
    path('', views.UserList.as_view(), name='myrecipes'),
    # path('createform/', views.UserList.as_view(), name='createform'),
]
