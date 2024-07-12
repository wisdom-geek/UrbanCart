from django.urls import path

from userauths import views

from django.contrib.auth import views as auth_views

app_name = 'userauths'

urlpatterns = [
    path('sign-up/', views.register_view, name='sign-up'),
     path('login/', views.login_view, name='login'),
     path('signout/', views.logout_view, name='signout'),
]
