from django.shortcuts import render

import re
from django.http import HttpResponse
from django.utils.timezone import datetime

def home(request):
    return render(request, "hello/home.html")

def about(request):
    return render(request, "hello/about.html")

def contact(request):
    return render(request, "hello/contact.html")

def hello_there(request, name):
    print(request.build_absolute_uri())
    return render(
        request,
        'hello/hello_there.html',
        {
            'name': name,
            'date': datetime.now()
        }
    )
