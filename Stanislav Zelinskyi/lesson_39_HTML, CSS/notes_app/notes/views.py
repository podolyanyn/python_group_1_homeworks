from django.shortcuts import render, redirect, get_object_or_404
from django.shortcuts import render, redirect
from .forms import NoteForm
from .models import Note


def index(request):
    return render(request, 'notes/index.html')


def note_list(request):
    notes = Note.objects.all()
    return render(request, 'notes/note_list.html', {'notes': notes})


def create_note(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('note_list')
    else:
        form = NoteForm()
    return render(request, 'notes/create_note.html', {'form': form})


def view_note(request, note_id):
    note = get_object_or_404(Note, id=note_id)
    return render(request, 'notes/view_note.html', {'note': note})
