from django.shortcuts import render, get_object_or_404, redirect
from .forms import NoteForm
from .models import Note


def create_note(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            text = form.cleaned_data['text']
            reminder = form.cleaned_data['reminder']
            category = form.cleaned_data['category']
            Note.objects.create(title=title, text=text, reminder=reminder, category=category)
            return redirect('note_list')
    else:
        form = NoteForm()
    return render(request, 'app_1/create_note.html', {'form': form})


def note_details(request, note_id):
    note = get_object_or_404(Note, pk=note_id)
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            note.title = form.cleaned_data['title']
            note.text = form.cleaned_data['text']
            note.reminder = form.cleaned_data['reminder']
            note.category = form.cleaned_data['category']
            note.save()
    else:
        form = NoteForm(initial={
            'title': note.title,
            'text': note.text,
            'reminder': note.reminder,
            'category': note.category
        })
    return render(request, 'app_1/note_details.html', {'form': form})


def note_list(request):
    notes = Note.objects.all()
    return render(request, 'app_1/note_list.html', {'notes': notes})


def delete_note(request, note_id):
    note = get_object_or_404(Note, pk=note_id)
    note.delete()
    return redirect('note_list')

