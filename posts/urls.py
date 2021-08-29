from django.urls import path
from . import views as post_views

#127.0.0.1:8000/posts/
urlpatterns=[
    path('<str:slug>/',post_views.post,name='post'),
    path('',post_views.index,name='posts')
]