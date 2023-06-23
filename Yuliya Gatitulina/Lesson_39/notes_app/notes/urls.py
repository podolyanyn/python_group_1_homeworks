from django.urls import path

from . import views

urlpatterns = [
    path("qwerty/", views.index, name="index"),
    path("", views.notes),
]