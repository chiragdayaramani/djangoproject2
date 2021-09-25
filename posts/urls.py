from collections import namedtuple
from django.urls import path
from . import views as post_views

#127.0.0.1:8000/posts/
urlpatterns=[
    path('',post_views.index,name='posts'),
    path('my_posts/',post_views.my_posts,name='my_posts'),
    path('category_posts/<str:slug>/',post_views.category_posts,name='category_posts'),
    path('listcategories/',post_views.listcategories,name='listcategories'),
    path('trash/',post_views.trash,name='trash'),
    path('restore/<str:slug>',post_views.restore,name='restore'),
    path('permanent_delete/',post_views.permanent_delete,name='permanent_delete'),
    path('create/',post_views.create,name='create'),
    path('createcategory/',post_views.createcategory,name='createcategory'),
    path('<str:slug>/update/',post_views.update,name='update'),
    path('delete/',post_views.delete,name='delete'),
    path('search/',post_views.search,name='search'),

    path('<str:slug>/',post_views.post,name='post'),
]