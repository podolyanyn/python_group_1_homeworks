from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from .models import Category, Notes
from django.template import loader
from django.urls import reverse
from .forms import NotesForm

def index(request):
    return HttpResponse("Hello! It's my first site.")

def notes(request):
    notes = Notes.objects.all()
    #notes = Notes.objects.select_related('categories').all()
    return render(request, 'notes/index.html', {'notes': notes})

def new_note(request):
    if request.method == 'POST':
        form = NotesForm(request.POST)
        if form.is_valid():
            n = Notes(category=form.cleaned_data['category'], title=form.cleaned_data['title'],
                         text=form.cleaned_data['text'], reminder=form.cleaned_data['reminder'])
            n.save()
            return HttpResponseRedirect('/notes/')
    else:
        form = NotesForm()
    return render(request, 'notes/new_note.html', {'form': form})

def change_note(request, note_id):
    note = get_object_or_404(Notes, pk=note_id)
    if request.method == 'POST':
        form = NotesForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/notes/')
    else:
        form = NotesForm(instance=note)
    return render(request, 'notes/change_note.html', {'form': form})

def delete_note(request, note_id):
    note = get_object_or_404(Notes, pk=note_id)
    note.delete()
    return HttpResponseRedirect('/notes/')
