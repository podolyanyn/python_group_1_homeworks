from django.http import HttpResponse
from django.shortcuts import render
from .models import Note, Categories


def first(request):
    return HttpResponse("Hello from the Notes app")

def index(request):
    notes = Note.objects.all()
    return render(request, 'notes/index.html', {'notes': notes})
