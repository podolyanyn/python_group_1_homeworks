from django.http import HttpResponse
from django.http import HttpResponseNotAllowed
from django.shortcuts import get_object_or_404, render, redirect
from .models import Notes, Categories
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .forms import NotesForm, RegistrationForm
from django_filters.views import FilterView
from .filters import ProductFilter
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.db.models import Q
from django.contrib.auth import login, logout, authenticate
import requests



def send_notes_to_telegram(request, note_id):
    if request.method == 'POST':
        note = get_object_or_404(Notes, pk=note_id)
        message = f"Ваша нотатка: \nNote categorie: {note.categories}\nNote title: {note.title}\nNote text: {note.text}\n" \
                  f"Note reminder: {note.reminder}"
        token = "6036572513:AAGvMHuJKqrC45QvIAEFStGPZozBJiHqmn0"
        url = "https://api.telegram.org/bot"
        channel_id = "409715641"
        url += token
        method = url + "/sendMessage"

        requests.post(method, data={
            "chat_id": channel_id,
            "text": message
        })
        return render(request, 'notes/send_to_telegram.html')

    return HttpResponse('Щось пішло не так')



@login_required
def notes(request):
    notes = Notes.objects.filter(Q(user=request.user) | Q(user=None))

    return render(request, 'notes/index.html', {'data': notes})

def sign_up(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/notes/')
    else:
        form = RegistrationForm()

    return render(request, 'registration/sign_up.html', {'form': form})


@login_required
def create_note(request):
    if request.method == 'POST':
        form = NotesForm(request.POST)
        if form.is_valid():
            # form.save()
            q = Notes(categories=form.cleaned_data['categories'], title=form.cleaned_data['title'],
                         text=form.cleaned_data['text'], reminder=form.cleaned_data['reminder'], user = request.user)
            q.save()

            # return redirect('notes/index.html')  # Перенаправлення на сторінку зі списком нотаток
            return HttpResponseRedirect('/notes/')
    else:
        form = NotesForm()

    return render(request, 'notes/create_note.html', {'form': form})


@login_required
def delete_note(request, note_id):
        if request.method == 'POST':
            note = Notes.objects.get(pk=note_id)
            note.delete()
            return redirect('/notes/')  # Перенаправлення на сторінку зі списком нотаток
        else:
            return HttpResponseRedirect('/notes/')  # Перенаправлення на головну сторінку, якщо метод не є POST


@login_required
def correct_note(request, note_id):
    note = get_object_or_404(Notes, pk=note_id)
    if request.method == 'POST':
        form = NotesForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/notes/')
    else:
        form = NotesForm(instance=note)

    return render(request, 'notes/correct_note.html', {'form': form})


def filter_notes(request):
    # f = ProductFilter(request.GET, queryset=Notes.objects.all())
    category = request.GET.get('category').capitalize()
    title = request.GET.get('title').capitalize()
    reminder = request.GET.get('reminder').capitalize()

    filtered_notes = Notes.objects.all()

    if category:
        filtered_notes = filtered_notes.filter(categories__title=category)
    if title:
        filtered_notes = filtered_notes.filter(title__icontains=title)
    if reminder:
        filtered_notes = filtered_notes.filter(reminder__icontains=reminder)


    return render(request, 'notes/filter_notes.html', {'notes': filtered_notes})


def find_notes(request):

    title = request.GET.get('title').capitalize()
    filtered_notes = Notes.objects.all()
    if title:
        filtered_notes = filtered_notes.filter(title__icontains=title)
    return render(request, 'notes/find_notes.html', {'notes': filtered_notes})


def search(request):
    query = request.GET.get('searching_text')
    results = Notes.Notes.objects.all()
    if query:
        results = Notes.objects.filter(title__icontains=query)

    context = {
        'results': results,
    }
    return render(request, 'notes/search.html', context)

