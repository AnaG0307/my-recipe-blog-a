from . import views
from django.urls import path


urlpatterns = [
    path('add-recipe/', views.add_recipe, name='add-recipe'),
    path('', views.UserList.as_view(), name='myrecipes'),
    path('urecipe_detail', views.urecipe_detail, name='urecipe_detail'),
    # path('<str:title>/', views.UserPost.as_view(), name='user_post'),
    # path('createform/', views.UserList.as_view(), name='createform'),
]
