from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from .models import Note
from .forms import NoteForm


def hello_view(request):
    return HttpResponse("Hello from Notes app.")


# def notes_view(request):
#     notes = [
#         {'name':'note_1', 'note':'this is note_1'},
#         {'name':'note_2', 'note':'this is note_2'},
#         {'name':'note_3', 'note':'this is note_3'},
#     ]
#     return render(request, 'notes/index.html', {'notes':notes})


def notes_view(request):
    notes = Note.objects.all()
    return render(request, 'notes/index.html', {'notes': notes})


def create_note_view(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/notes/')  # перенаправлення на список нотаток
    else:
        form = NoteForm()
    return render(request, 'notes/create_note.html', {'form': form})

def note_detail_view(request, note_id):
    note = get_object_or_404(Note, id=note_id)

    if request.method == 'POST':
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/notes/')  # перенаправлення на список нотаток
    else:
        form = NoteForm(instance=note)

    return render(request, 'notes/note_detail.html', {'form': form, 'note': note})

def delete_note_view(request, note_id):
    note = get_object_or_404(Note, id=note_id)
    if request.method == 'POST':
        note.delete()
        return redirect('/notes/')  # перенаправлення на список нотаток
    return render(request, 'notes/delete_note.html', {'note': note})