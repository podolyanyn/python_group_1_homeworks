from django.urls import path
from . import views

urlpatterns = [
    path("hello/", views.index, name="index"),
    path("", views.notes, name="notes"),
    path('new/', views.new_note, name='new_note'),
    path('<int:note_id>/delete/', views.delete_note, name='delete_note'),
    path('<int:note_id>/change/', views.change_note, name='change_note'),
    ]