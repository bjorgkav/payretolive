from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import login, logout, authenticate

def index(request):
    if request.method == "POST":
        #authenticate the user
        return render(request, "index.html", context={})
    
    return render(request, "index.html", context={})