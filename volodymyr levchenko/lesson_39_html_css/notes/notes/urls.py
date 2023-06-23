from django.urls import path
from .views import hello_view, notes_view

app_name = 'notes'

urlpatterns = [
    path('notes_hello/', hello_view, name='notes_hello'),
    path('', notes_view),
]