from django.urls import path
from flashkicks_app import views 

urlpatterns = [
    path('', views.index),
    path('signupbtn', views.signupbtn),
    path('loginbtn', views.loginbtn),
    path('signup_page', views.signup_page),
    path('login_page', views.login_page),
    path('signup', views.signup),
    path('login', views.login),
    path('dashboard', views.dashboard)
]
