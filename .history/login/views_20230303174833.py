from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User

def index(request):
    return render(request, "index.html", context={})
    
def success(request):
    if request.method == "POST":
        #authenticate the user
        #if authenticated successfully, send to logged in page
        username = request.POST["username"]
        password = request.POST["password"]
        #user = authenticate(username, password)
        return render(request, "success.html", context={'username':username, 'password':password})
    return redirect(reverse("login:index"))