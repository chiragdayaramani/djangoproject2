from users.views import logout
from django.contrib import auth
from django.contrib.auth import views as auth_views
from django.urls import path
from . import views as user_views

urlpatterns = [
    path("login/",auth_views.LoginView.as_view(template_name='login.html'),name='login'),
    path("logout/",user_views.logout,name='logout')
]
