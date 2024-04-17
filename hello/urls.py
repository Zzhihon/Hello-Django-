from django.urls import path
from hello import views
from django.shortcuts import render

urlpatterns = [
    path("hello/<name>", views.hello_there, name="hello_there"),
    path("about/" , views.about, name="about"),    
    path("", views.home, name="home"),
    path("contact/" , views.contact, name="contact"),
]
