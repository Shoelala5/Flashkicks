from django.urls import path
from flashkicks_app import views 

urlpatterns = [
    path('',views.index),
]
