from django.urls import path
from . import views
from django.conf import settings

urlpatterns = [
path('', views.getData),
path('posts/', views.postData, name='posts'),
]