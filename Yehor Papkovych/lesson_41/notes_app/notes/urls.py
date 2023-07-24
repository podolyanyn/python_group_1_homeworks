from django.urls import path
from .views import create_note, index, note_info, delete_note

from . import views

urlpatterns = [
    path('', index, name='index'),
    path('create/', create_note, name='create_form'),
    path('note/<int:note_id>/', note_info, name='note_info'),
    path('note/<int:note_id>/delete', delete_note, name='delete_note'),
]