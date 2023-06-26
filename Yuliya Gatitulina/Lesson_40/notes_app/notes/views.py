from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render

from .models import Category, Notes

def index(request):
    return HttpResponse("Hello! It's my first site.")


def notes(request):
    notes = Notes.objects.all()
    #notes = Notes.objects.select_related('categories').all()
    return render(request, 'notes/index.html', {'notes': notes})

