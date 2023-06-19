from django.http import HttpResponse
# from django.contrib.auth.models import User
from django.shortcuts import render
from .models import Notes, Categories

def index(request):
    return HttpResponse("Hello from Notes app.")


def notes(request):
    notes = Notes.objects.select_related('categories').all()
    return render(request, 'notes/index.html', {'data': notes})
