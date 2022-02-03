from django import http
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "learning/index.html")

def greet(request, name):
    return render(request, "learning/greet.html", {
        "name": name.capitalize()
    })