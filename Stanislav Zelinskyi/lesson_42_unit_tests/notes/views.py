from django.shortcuts import render, redirect, get_object_or_404
from .forms import NoteForm, CategoryForm
from .models import Note, Category
from django.utils.dateparse import parse_date, parse_time


def index(request):
    categories = Category.objects.all()
    return render(request, 'notes/index.html', {'categories': categories})


def note_list(request):
    notes = Note.objects.all()
    return render(request, 'notes/note_list.html', {'notes': notes})


def create_note(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            reminder_date = form.cleaned_data['reminder_date']
            reminder_time = form.cleaned_data['reminder_time']
            note.reminder_date = parse_date(str(reminder_date)) if reminder_date else None
            note.reminder_time = parse_time(str(reminder_time)) if reminder_time else None
            note.save()
            # Add your logic for setting the reminder here
            return redirect('note_list')
    else:
        form = NoteForm()
    return render(request, 'notes/create_note.html', {'form': form})


def view_note(request, note_id):
    note = get_object_or_404(Note, id=note_id)
    return render(request, 'notes/view_note.html', {'note': note})


def edit_note(request, note_id):
    note = get_object_or_404(Note, id=note_id)
    if request.method == 'POST':
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('view_note', note_id=note.id)
    else:
        form = NoteForm(instance=note)
    return render(request, 'notes/edit_note.html', {'form': form, 'note': note})


def delete_note(request, note_id):
    note = get_object_or_404(Note, id=note_id)
    if request.method == 'POST':
        note.delete()
        return redirect('note_list')
    return render(request, 'notes/delete_note.html', {'note': note})


def create_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('create_category')
    else:
        form = CategoryForm()
    return render(request, 'notes/create_category.html', {'form': form, 'categories': Category.objects.all()})


def delete_category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    category.delete()
    return redirect('create_category')


def filter_notes(request):
    categories = Category.objects.all()
    notes = Note.objects.all()

    # Получаем параметры фильтрации из GET-запроса
    category_id = request.GET.get('category')
    reminder_date = request.GET.get('reminder_date')
    created_at = request.GET.get('created_at')

    # Применяем фильтры к заметкам
    if category_id:
        notes = notes.filter(category_id=category_id)
    if reminder_date:
        notes = notes.filter(reminder_date=reminder_date)
    if created_at:
        notes = notes.filter(created_date=created_at)

    return render(request, 'notes/filter_notes.html', {
        'categories': categories,
        'notes': notes,
        'selected_category': int(category_id) if category_id else None,
        'selected_reminder_date': reminder_date,
        'selected_created_at': created_at,
    })


def search_notes(request):
    query = request.GET.get('query')  # Получаем значение поискового запроса из параметра 'query'
    notes = Note.objects.filter(title__icontains=query) if query else []
    return render(request, 'notes/search_notes.html', {'notes': notes, 'query': query})
