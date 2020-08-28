# mysite/blog/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),   #This means if you go to http://127.0.0.1/8000. It will take you to this url
    path('post/<int:pk>/', views.post_detail, name='post_detail')
]