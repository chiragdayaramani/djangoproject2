from collections import namedtuple
from django.urls import path
from . import views as post_views

#127.0.0.1:8000/posts/
urlpatterns=[
    path('',post_views.index,name='posts'),
    path('my_posts/',post_views.my_posts,name='my_posts'),
    path('create/',post_views.create,name='create'),
    path('createcategory/',post_views.createcategory,name='createcategory'),
    path('<str:slug>/update/',post_views.update,name='update'),
    path('<str:slug>/',post_views.post,name='post'),
]