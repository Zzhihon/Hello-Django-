from django.urls import path
from hello import views
from django.shortcuts import render
from hello.models import LogMessage

data_list_view = views.DataListView.as_view(
    queryset=LogMessage.objects.order_by("-log_date")[:5],  # :5 limits the results to the five most recent
    context_object_name="message_list",
    template_name="hello/data.html",
)

urlpatterns = [
    path("hello/<name>", views.hello_there, name="hello_there"),
    path("about/" , views.about, name="about"),
    path("data/", data_list_view, name="data"),
    path("", views.home, name="home"),
    path("contact/" , views.contact, name="contact"),
    path("log_success/", views.log_success, name="log_success"),
    path("log/", views.log_message, name="log"),
]
