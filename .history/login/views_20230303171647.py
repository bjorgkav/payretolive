from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User

def index(request):
    if request.method == "POST":
        #authenticate the user
        #if authenticated successfully, send to logged in page
        return render(request, "index.html", context={})
    
    return render(request, "index.html", context={})

def register(request):
    if request.method == "POST":
        new_user = 