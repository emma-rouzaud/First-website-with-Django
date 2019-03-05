# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

# def index(request):
#     return HttpResponse('<h1>Welcome</h1>')


# def index(request):
#     now = datetime.now()
#
#     html_content = "<html><head><title>Hello, Django</title></head><body>"
#     html_content += "<strong>Hello Django!</strong> on " + now.strftime("%A, %d %B, %Y at %X")
#     html_content += "</body></html>"
#
#     return HttpResponse(html_content)

def index(request):
    now = datetime.now()

    return render(
        request, "blog/index.html",
        {
            'title' : "Welcome to Django",
            'message' : "Welcome to Django!",
            'content' : " on " + now.strftime("%A, %d %B, %Y at %X")
        }
    )

def about(request):
    return render(
        request, "blog/about.html",
        {
            'title' : "About blog",
            'content' : "Example app page for Django."
        }
    )
