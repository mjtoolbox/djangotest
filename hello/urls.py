from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("echo/<str:message>", views.echo, name="echo"),
    path("greet/<str:name>", views.greet, name="greet")
]