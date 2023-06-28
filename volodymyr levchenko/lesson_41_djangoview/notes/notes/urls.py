from django.urls import path
from .views import hello_view, notes_view, create_note_view, note_detail_view, delete_note_view

app_name = 'notes'

urlpatterns = [
    path('notes_hello/', hello_view, name='notes_hello'),
    path('', notes_view),
    path('create/', create_note_view, name='create_note'),
    path('note/<int:note_id>/', note_detail_view, name='note_detail'),
    path('note/<int:note_id>/delete/', delete_note_view, name='delete_note'),
]