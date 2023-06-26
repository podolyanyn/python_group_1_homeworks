from django.shortcuts import render
from .models import Note


def home(request):
    notes = Note.objects.all()  # Отримати всі записи з таблиці нотаток
    return render(request, 'app_1/home.html', {'notes': notes})
