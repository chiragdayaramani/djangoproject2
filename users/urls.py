from django.contrib import auth
from django.contrib.auth import views as auth_views
from django.urls import path


urlpatterns = [
    path("login/",auth_views.LoginView.as_view(template_name='login.html'),name='login'),
    path("logout/",auth_views.LoginView.as_view(template_name='logout.html'),name='logout')
]
