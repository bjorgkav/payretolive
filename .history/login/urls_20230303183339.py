from django.urls import path
from . import views

app_name='login' #required for redirects, adding namespaces to project URLS

urlpatterns = [
    path("", views.index, name="index"),
    path("success/", views.success, name="success"),
]