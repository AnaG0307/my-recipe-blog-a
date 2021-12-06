from . import views
from django.urls import path


urlpatterns = [
    path('', views.Recipe_List_View.as_view(), name='home'),
]
