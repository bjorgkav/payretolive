from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import login, logout, authenticate

def index(request):
    
    return render(request, "index.html", context={})