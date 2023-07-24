from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from .models import Note
from .forms import NoteForm


def first(request):
    return HttpResponse("Hello from the Notes app")

def index(request):
    notes = Note.objects.all()
    return render(request, 'notes/index.html', {'notes': notes})

def create_note(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/notes/')
    else:
        form = NoteForm()
    return render(request, 'notes/create_note.html', {'form': form})

def delete_note(request, note_id):
    note = get_object_or_404(Note, id=note_id)
    if request.method == 'POST':
        note.delete()
        return redirect('/notes/')
    return render(request, 'notes/delete_note.html', {'note': note})

def note_info(request, note_id):
    note = get_object_or_404(Note, id=note_id)
    if request.method == 'POST':
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/notes/')
    else:
        form = NoteForm(instance=note)
    return render(request, 'notes/note_info.html', {'form': form, 'note': note})