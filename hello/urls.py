from django.urls import path
from hello import views
from django.shortcuts import render

urlpatterns = [
    path("", views.home, name="home"),
    path("hello/<name>", views.hello_there, name="hello_there"),
    path("home/radein/hello_django/about" , views.about, name="about"),
    path("home/radein/hello_django/contact" , views.contact, name="contact"),
]
